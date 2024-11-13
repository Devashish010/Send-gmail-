import smtplib

# set up the smtp server

smtp_server="smtp.gmail.com"
port = 587 # for starttls
sender_email = "example_1@gmail.com" # your email address
password = "exampl1_1_otp_app"# email acc password

# create the email

reciever_email = "example_2@gmail.com" # reciever email
subject = "test email !"
body = "this is text email from python!!"

#constructr the email message
message = f"subject: {subject}\n\n{body}"

try:
    #start the server
    server = smtplib.SMTP(smtp_server,port)
    server.starttls()# upgrade to a secure connection
    server.login(sender_email,password)# log in to the server

    # send the email
    server.sendmail(sender_email,reciever_email,message)
    print("email sent successfully!")

except Exception as e:
    print(f"Error occured:{e}")

finally:
    server.quit()   # close the connection


    
