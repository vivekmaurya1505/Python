import smtplib
sender_mail = input("Enter your gmail:")
receivers_mail = input("Enter receivers gmail:")

message = """ From: From Person %s
To: To Person %s
Subject : Sending SMTP e-mail
This is a test r-mail message.
"""%(sender_mail,receivers_mail)
