def build_email_prompt(
        sender_name,
        recipient,
        email_type,
        tone,
        purpose,
        start_date,
        end_date
):
    return f"""
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