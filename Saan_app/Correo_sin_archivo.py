import smtplib
 
server = smtplib.SMTP(host='smtp-relay.gmail.com',port=587)

# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Le estoy mandando un correo desde Python"
 
# setup the parameters of the message
password = "unicornio"
msg['From'] = "juannaruto2012@gmail.com"
msg['To'] = "esantosr@unal.edu.co"
msg['Subject'] = "archivo_Python"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print "successfully sent email to %s:" % (msg['To'])