import smtplib
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login('prattiaditya@gmail.com', 'iamcooL9')

smtp_server.sendmail('prattiaditya@gmail.com', 'rishita1019@gmail.com', 'Subject: Happy Tuesday!\n PLease send email daily with updates ')

smtp_server.quit()
print('Email sent successfully')
