import yagmail
import os

sender = os.getenv("SENDER")
receiver = os.getenv("RECEIVER")

subject = "RE: This is the subject"

contents = """
Hi,

Here is the content of the email.

Thank you!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
