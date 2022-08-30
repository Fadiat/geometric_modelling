import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['fadi.atallah7@gmail.com']
msg = MIMEMultipart()
sender = 'fadi@atallah.co.uk'
subject = "My subject"
body = "This is my email body"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
#print text
# Send the message via our SMTP server
s = smtplib.SMTP('smtp.office365.com')
s.sendmail(sender,address_book, text)
s.quit()