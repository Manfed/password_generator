import smtplib
from email.message import EmailMessage

from password_generator.utils.constants import GMAIL_USERNAME, GMAIL_PASSWORD, MAIL_SUBJECT, MAIL_CONTENT, \
    FEEDBACK_FORM_URL


def send_mail(to: str, uuid: str, after_days: int):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.login(GMAIL_USERNAME, GMAIL_PASSWORD)

            message = __create_message(to, after_days, uuid)
            server.send_message(message)
    except:
        print('Unable to send an email to %s' % to)


def __create_message(to: str, days: int, uuid: str):
    message = EmailMessage()
    message.set_content(MAIL_CONTENT % (FEEDBACK_FORM_URL, uuid))
    message['Subject'] = MAIL_SUBJECT % days
    message['From'] = GMAIL_USERNAME
    message['To'] = to
    return message
