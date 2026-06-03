import streamlit as st

from services.gemini_service import generate_email
from prompts.email_prompt import build_email_prompt
from utils.validators import validate_inputs

if st.button("Generate Email"):

    is_valid, message = validate_inputs(
        sender_name,
        recipient,
        purpose
    )

    if not is_valid:
        st.warning(message)

    else:

        prompt = build_email_prompt(
            sender_name,
            recipient,
            email_type,
            tone,
            purpose,
            start_date,
            end_date
        )

        try:

            with st.spinner("Generating email..."):

                email = generate_email(prompt)

            st.success("Email Generated Successfully!")

            st.text_area(
                "Generated Email",
                value=email,
                height=350
            )

            st.download_button(
                "📥 Download Email",
                email,
                file_name="generated_email.txt",
                mime="text/plain"
            )

        except Exception:
            st.error(
                "Gemini service temporarily unavailable."
            )