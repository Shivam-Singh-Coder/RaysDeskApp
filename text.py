import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg.set_content("Hii")
msg['Subject']='Raj'
msg['From']='shivamsinghballia2003@gmail.com'
msg['To']='sudhanshukumar2207@gmail.com'

# s=smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()
s=smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login('shivamsinghballia2003@gmail.com','Shivam&1945')
s.send_message(msg)
s.quit()