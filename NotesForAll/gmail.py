import smtplib
import os

try:
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()

		smtp.login(email,password)

		subject = ''
		body = ''

		msg = 'Subject:{subject}\n\n{body}'

		smtp.sendmail(sender_email,receiver_email,msg)

		print('email sent')
except:

	print('email failed')
	# sender_email and password should be grabbed by env. variable