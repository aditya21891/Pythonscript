
from email.headerregistry import Address
from email.message import EmailMessage
import os
import smtplib

# Gmail details
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

# Recipent
to_address = (
    Address(display_name='Daily update', username='rishita1019', domain='gmail.com'),
)


def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg


if __name__ == '__main__':
    msg = create_email_message(
        from_address=email_address,
        to_address=to_address,
        subject='Daily tasks',
        body="Let me know what you did today using Python and Linux, I want every day mail of your daily updates",
    )

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(email_address, email_password)
        smtp_server.send_message(msg)

    print('Email sent successfully')
