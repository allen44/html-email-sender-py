import smtplib
from email.message import EmailMessage
from sys import argv
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
print(html)

email = EmailMessage()
email['from'] = input('From:   ')
email['to'] = input('To:   ')
email['subject'] = input('Subject:   ')
email.set_content(html.substitute({'name': 'Tintin'}), 'html')
print(email.get_content())

print(email)

try:
    username = argv[1]
    password = argv[2]
except:
    username = input('username:   ')
    password = input('Password:   ')



with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.send_message(email)
    print('all good. Message sent.')
