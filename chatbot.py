import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ Google API key not found. Please check your .env file.")

# 2. Configure Gemini
genai.configure(api_key=api_key)

# 3. Create model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# 4. Chat loop
def chat():
    print("🤖 Gemini AI Assistant (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Assistant: Goodbye 👋")
            break
        try:
            response = model.generate_content(user_input)
            print("Assistant:", response.text)
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    chat()
