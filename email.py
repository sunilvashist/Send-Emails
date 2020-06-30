import smtplib
from email.message import EmailMessage
import random

email = EmailMessage()
email['from'] = 'hacker'
email['to'] = '{reciever-mail_id}'
email['subject'] = 'hello sir , testing'
#set content for 
email.set_content('hello sir')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('{your mail_id}', '{your mail-password}')
    
     smtp.send_message(email)
     print("all good" )
     
    # if want to send number of times
    #for i in range(1000):

     #   smtp.send_message(email)
     #   print("total :", i)
