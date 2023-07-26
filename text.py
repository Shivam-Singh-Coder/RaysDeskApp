# import smtplib
# from email.message import EmailMessage
# msg=EmailMessage()
# msg.set_content("Hii")
# msg['Subject']='Raj'
# msg['From']='shivamsinghballia2003@gmail.com'
# msg['To']='sudhanshukumar2207@gmail.com'

# # s=smtplib.SMTP('localhost')
# # s.send_message(msg)
# # s.quit()
# s=smtplib.SMTP_SSL('smtp.gmail.com',465)
# s.login('shivamsinghballia2003@gmail.com','Shivam&1945')
# s.send_message(msg)
# s.quit()
import datetime
# print(datetime.datetime.now().strftime("07"))
# import calendar
# month_number = int(input("Enter month number: "))
# print(calendar.day_abbr[month_number])
# def to_date(num_str):
#     return datetime.datetime.strptime(num_str,"%d%m%Y")
# to_date("2023-7-22")
from datetime import datetime
print(datetime.strptime('2023-07-22', '%Y-%m-%d').strftime('%d %b %Y'))