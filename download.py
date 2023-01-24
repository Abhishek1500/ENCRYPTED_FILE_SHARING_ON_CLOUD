from email.message import EmailMessage
import ssl
import smtplib
emailsender='abhishekparmar1500@gmail.com'
emailpass='skpquyrpswjqaljx'
emailreciver='hiyisor930@kixotic.com'

subject="keys for file access"

body="hello"

em=EmailMessage()
em['from']=emailsender
em['to']=emailreciver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(emailsender,emailpass)
    smtp.sendmail(emailsender,emailreciver,em.as_string())
    
print("mail sent")
