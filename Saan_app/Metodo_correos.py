import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class nota:
	def __init__():
		self.asignatura = asignatura
		self.nota= nota
		self.correo_estudiante = correo_estudiante
		self.operacion= operacion
	@staticmethod	
	def enviar_correos(asignatura, nota, correo_estudiante, operacion):
		server = smtplib.SMTP(host='smtp-relay.gmail.com',port=587)
		print ("inicio sesion")
		if (operacion =="modificar nota"):
			message = "Se le ha modificado la nota " + nota + " a la siguiente asignatura: "+ asignatura
 		elif operacion=="agregar nota":
 			message = "Se le ha agregado la nota " + nota + " a la siguiente asignatura: "+ asignatura
		else:
			message = "se le ha borrado la nota" + nota + " a la siguiente asignatura: "+ asignatura
		password = "NOTASCLASE"
		msg['From'] = "saan.aplicacion@gmail.com"
		msg['To'] = correo_estudiante
		msg['Subject'] = "Su asignatura recibio cambios"
 		msg.attach(MIMEText(message, 'plain'))
 
		#create server
		server = smtplib.SMTP('smtp.gmail.com: 587')
 		server.starttls()
		print(server.starttls())
 
		# Login Credentials for sending the mail
		server.login(msg['From'], password)
 
 
		# send the message via the server.
		server.sendmail(msg['From'], msg['To'], msg.as_string())
 
		server.quit()
 
		print "successfully sent email to %s:" % (msg['To'])

Esteban=nota(raw_input(), raw_input(), raw_input(), raw_input() )
print(Esteban)
enviar_correos(Esteban)