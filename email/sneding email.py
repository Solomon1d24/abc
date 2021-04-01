import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path  

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Solomon Chow'
email['to'] = 'solomon1d24@gmail.com'
email['subject'] = 'Hey, It is a test!'

email.set_content(html.substitute({'name' : 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('solomon1d24@gmail.com', '56047550')
    smtp.send_message(email)
    print('all done!')


