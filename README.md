# Egyptian Hate Speech Detector 🇪🇬
مشروع كشف خطاب الكراهية بالعامية المصرية باستخدام الذكاء الاصطناعي.

## 🚀 كيفية الربط مع الموقع (API)
يا شباب الـ Back-end، استخدموا الكود ده عشان تبعتوا النصوص للموديل وتعرفوا النتيجة:

```python
from gradio_client import Client

# الربط مع السيرفر المرفوع على Hugging Face
client = Client("Abdelrazek-123/Hate-Speech-Detector")
result = client.predict(
    text="الجملة المراد فحصها",
    api_name="/predict"
)
print(result)
