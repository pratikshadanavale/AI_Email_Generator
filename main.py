import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

email_type = input("Enter Email Type: ")
tone = input("Enter Tone: ")
recipient = input("Recipient Name: ")
purpose = input("Purpose: ")

prompt = f"""
Generate a professional email.

Email Type: {email_type}
Tone: {tone}
Recipient: {recipient}
Purpose: {purpose}

Generate:
1. Subject Line
2. Email Body
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nGenerated Email:\n")
print(response.text)