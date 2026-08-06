import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

print("Models available to this API key:\n")
for m in client.models.list():
    print(m.name)