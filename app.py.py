import streamlit as st
from transformers import pipeline
import os

st.set_page_config(page_title="AI Hate Speech Detector", page_icon="🛡️")

# ستايل الألوان اللي إنت عايزها بالظبط (صناديق عريضة وواضحة)
st.markdown("""
    <style>
    .big-font { font-size:30px !important; font-weight: bold; text-align: center; color: white; padding: 20px; border-radius: 15px; }
    .bg-red { background-color: #FF0000; }
    .bg-yellow { background-color: #FFCC00; color: black !important; }
    .bg-green { background-color: #008000; }
    .stTextArea textarea { text-align: right; direction: rtl; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ رادار كشف الإساءة ضد المرأة")

@st.cache_resource
def load_model():
    # تأكد إن ده اسم الفولدر اللي جنبك
    return pipeline("text-classification", model="./my_marbert_model")

if os.path.exists("./my_marbert_model"):
    classifier = load_model()
    text = st.text_area("أدخل النص هنا للفحص:", height=150)

    if st.button("حلل النص"):
        if text.strip():
            prediction = classifier(text)[0]
            label = prediction['label'].upper()
            score = prediction['score']

            # سطر التشخيص (ده اللي هيعرفنا الموديل بيفكر إزاي)
            st.info(f"الموديل باعت كود: {label} | بنسبة ثقة: {score:.2%} ")

            # تنفيذ طلبك بالألوان
            if "2" in label or "HATE" in label:
                st.markdown('<div class="big-font bg-red">❌ النتيجة: خطاب كراهية</div>', unsafe_allow_html=True)
                st.snow()
            elif "1" in label or "OFFENSIVE" in label:
                st.markdown('<div class="big-font bg-yellow">⚠️ النتيجة: نص مسيء</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="big-font bg-green">✅ النتيجة: نص سليم</div>', unsafe_allow_html=True)
                st.balloons()
        else:
            st.warning("ادخل نصاً أولاً!")
else:
    st.error("❌ مشكلة: فولدر my_marbert_model مش موجود جنب الـ app.py")