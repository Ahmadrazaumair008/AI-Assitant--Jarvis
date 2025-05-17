# pip install google-generativeai
import google.generativeai as genai


# Replace with your actual API key
genai.configure(api_key="AIzaSyC9_1nhVulsVbGd8gzKFZDod54bWfEmZCM")

# Select a Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Send a request
response = model.generate_content("Who was the former prime minister of Pakistan")
print(response.text)