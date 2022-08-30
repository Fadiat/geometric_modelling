from mailer import Mailer
from mailer import Message

message = Message(From="fadi@atallah.co.uk",
                  To="fadi@atallah.co.uk",
                  charset="utf-8")
message.Subject = "An HTML Email"
message.Html = """This email uses <strong>HTML</strong>!"""
message.Body = """This is alternate text."""

sender = Mailer('smtp.office365.com')
sender.send(message)