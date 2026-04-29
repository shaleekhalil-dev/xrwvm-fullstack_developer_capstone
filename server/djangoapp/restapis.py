import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    """
    دالة لإرسال طلبات GET إلى الخلفية (Backend)
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {}".format(request_url))
    try:
        # إرسال طلب GET واسترجاع النتيجة كـ JSON
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        # في حال حدوث خطأ في الشبكة
        print(f"Network exception occurred: {err}")

def analyze_review_sentiments(text):
    """
    دالة لإرسال النص إلى ميكروسيرفس تحليل المشاعر
    """
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # إرسال النص للتحليل
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    """
    دالة لإرسال مراجعة جديدة (Review) إلى قاعدة البيانات عبر POST
    """
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")