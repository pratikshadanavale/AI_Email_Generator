import os
from dotenv import load_dotenv
from google import genai
import streamlit as st

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("📧 AI Email Generator")

email_type = st.selectbox(
    "Email Type",
    [
        "Leave Request",
        "Job Application",
        "Meeting Request",
        "Follow Up",
        "Resignation",
        "General"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Confident"
    ]
)

recipient = st.text_input("Recipient Name")
sender_name = st.text_input("Your Name")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
purpose = st.text_area("Purpose")

if st.button("Generate Email"):
    prompt = f"""
    Generate a complete professional email.

    Details:
    Sender Name: {sender_name}
    Recipient: {recipient}
    Email Type: {email_type}
    Tone: {tone}
    Purpose: {purpose}
    Start Date: {start_date}
    End Date: {end_date}

    Rules:
    1. Do not use placeholders.
    2. Use actual provided information.
    3. Generate a clear subject.
    4. Generate complete email ready to send.
    5. Format professionally.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.subheader("Generated Email")

        st.text_area(
            "Generated Email",
            value=response.text,
            height=350
        )

        st.download_button(
            "📥 Download Email",
            data=response.text,
            file_name="generated_email.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error generating email: {e}")