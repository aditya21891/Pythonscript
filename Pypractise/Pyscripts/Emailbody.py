import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "prattiaditya@gmail.com"
receiver_email = "rishita1019@gmail.com"
password = input("Enter your password here: ")
message = """\
Subject: Hi there
From:{}
To:{}
This Sample  E-Mail  is sent from Python.""".format(sender_email,receiver_email)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print ('It worked')
