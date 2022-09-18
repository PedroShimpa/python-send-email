import smtplib, ssl

# configuração
smtp_server = "smtp.gmail.com"
port = 587  
sender_email = "email@gmail.com"
pass_email = "your_pass"
message = input('Digite sua Mensagem:')


context = ssl.create_default_context()

server = smtplib.SMTP(smtp_server,port)
try:
    server.ehlo() 
    server.starttls(context=context) #protege a conexão
    server.ehlo() 
    server.login(sender_email, 'smtpass')
    server.sendmail(sender_email, 'falconipedro4@gmail.com', message)
    print('Email Enviado')
    server.quit() 
except Exception as e:
    print(e)
