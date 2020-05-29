import smtplib
sender_mail = input("Enter your gmail:")
receivers_mail = input("Enter receivers gmail:")

message = """ From: From Person %s
To: To Person %s
Subject : Sending SMTP e-mail
This is a test r-mail message.
"""%(sender_mail,receivers_mail)

#try:
password = input("Enter the password:")
smtpObj = smtplib.SMTP("smtp.gmail.com",587)
smtpObj.starttls()
smtpObj.login(sender_mail,password )
smtpObj.sendmail(sender_mail,receivers_mail,message)
print("Sucessfully sent mail")
#except Exception:
#    print("Error: Unable to send email")


#Not Completed
