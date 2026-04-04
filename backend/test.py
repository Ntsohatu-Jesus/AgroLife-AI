import google.generativeai as genai

genai.configure(api_key="AIzaSyAeRSgfCY4BliiFAztwiGIJXmAKXWDOzDo")

for m in genai.list_models():
    print(m.name)