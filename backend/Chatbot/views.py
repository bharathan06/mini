from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
def chat_with_gemini(user_input):
    response = model.generate_content(user_input)
    return response.text

