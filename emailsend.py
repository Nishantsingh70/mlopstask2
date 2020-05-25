import smtplib

sender_email = "nishantsingh70600@gmail.com"
receiver_email = "nishantsingh9527@gmail.com"
password = input(str("Please enter the password"))
message = "Model is Successfully created"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(sender_email,password)
print('login successfully')

server.sendmail(sender_email, receiver_email , message)
print("Email has been sent to ", receiver_email)
server.quit()
