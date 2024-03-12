import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

def send_notification(subject: str, body: str):
    load_dotenv()

    if os.environ.get("ENVIRONMENT") == "development":
        """If it's development environment, print the email instead of sending it."""
        print(f"Subject: {subject}\n\n{body}")
        print("-------------------------")
        return

    email_sender = os.environ.get("EMAIL_SENDER")
    email_password = os.environ.get("EMAIL_PASSWORD")
    email_receiver = os.environ.get("EMAIL_RECEIVER")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
