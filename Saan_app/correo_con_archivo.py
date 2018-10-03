# importamos smtplib
import smtplib
 
server = smtplib.SMTP(host='smtp-relay.gmail.com',port=587)
# importamos los paquetes
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# creamos el objeto mensaje
msg = MIMEMultipart()
message = "Mensaje a enviar" 
 
# organizamos los parametros
password = "contraseña"
msg['From'] = "Correo bot"
msg['To'] = "correo del estudiante"
msg['Subject'] = "asunto"

# cuerpo del mensaje
msg.attach(MIMEText(message, 'plain'))
# attach image to message body
msg.attach(MIMEImage(file("archivo.loquesea").read()))

 
# creamos el servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# ingresamos credenciales
server.login(msg['From'], password)
 
 
# mandamos el mensaje por el servidor
server.sendmail(msg['From'], msg['To'], msg.as_string())
# cerramos el servidor
server.quit()
# todo salio bien
print "successfully sent email to %s:" % (msg['To'])