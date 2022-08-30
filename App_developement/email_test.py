# email test

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import re
from validate_email import validate_email

# part 1 if passed go to next step

def check(email):

  valid_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(valid_regex, email)):

    print("This is a valid email")

  else:

    print("This is an invalid email")

email = "correctemail@gmail.com"



def check_2(email):
    valid_email = validate_email(email_address='fasdsadsifdsddddda@gmail.com', check_smtp = True)
    print("dff", valid_email)

# Mail Check if correct:
# check(email)
# check_2(email)



# step 3 make an email server:



from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import smtplib, ssl

from email import encoders


# port = 995
#
# server = "outlook.office365.com"
# # server = "smtp.office365.com"
#
# sender = "fadi@atallah.co.uk"
#
# recipient = "fadi.atallah21@imperial.ac.uk"
#
# password = "Fadi@0795294118"
#
# msg = MIMEMultipart()
#
# message = "This email includes an attachment"
#
# msg.attach(MIMEText(message, "plain"))
#
# filename = "database.py"
#
# with open(filename, "rb") as pdf:
#
#     attachment = MIMEBase("application", "octet-stream")
#
#     attachment.set_payload(pdf.read())
#
# encoders.encode_base64(attachment)
#
# attachment.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )
#
# msg.attach(attachment)
#
#
# SSLcontext = ssl.create_default_context()
#
# with smtplib.SMTP(server, port) as server:
#
#     server.starttls(context=SSLcontext)
#
#     server.login(sender, password)
#
#     server.sendmail(sender, recipient, msg.as_string())


# import the smtplib module. It should be included in Python by default
SERVER = "smtp.office365.com"
FROM = "fadi@atallah.co.uk"
TO = ["fadi.atallah7@gmail.com"] # must be a list

SUBJECT = "Hello!"
TEXT = "This is a test of emailing through smtp of example.com."

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.login("MrDoe", "PASSWORD")
server.sendmail(FROM, TO, message)
server.quit()
