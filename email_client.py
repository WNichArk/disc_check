import smtplib as sl
import constants.constants as cs
from email.message import EmailMessage


def send_message(to_emails, subject, message):
    s = sl.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(cs.GSU, cs.GSP)
    mess = EmailMessage()
    mess["Subject"] = subject
    mess["From"] = cs.GSU
    mess["To"] = to_emails
    mess.set_content(message)

    s.send_message(mess)
    s.quit()


