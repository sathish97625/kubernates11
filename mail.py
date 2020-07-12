import smtplib

sender_email = "shwetanice1997@gmail.com"
rec_email = "bhardwajsaurabh023@gmail.com"
password = "********"
message = " Your website has some error......plz check the code and push again"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
