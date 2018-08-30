import logging
import smtplib
from email.message import EmailMessage

from password_generator.utils.constants import GMAIL_USERNAME, GMAIL_PASSWORD, MAIL_SUBJECT, MAIL_CONTENT, \
    FEEDBACK_FORM_URL


def send_test_mail(to: str, uuid: str, after_days: int):
    content = MAIL_CONTENT % (FEEDBACK_FORM_URL, uuid)
    subject = MAIL_SUBJECT % after_days
    sender = GMAIL_USERNAME
    recipient = to
    send_mail(subject, content, sender, recipient)


def send_mail(subject: str, content: str, sender: str, recipient: str):
    logger = logging.getLogger('email_sender')
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.login(GMAIL_USERNAME, GMAIL_PASSWORD)

            message = __create_message(subject, content, sender, recipient)

            server.send_message(message)
            logger.info('Mail has been sent.')
    except:
        logger.error('Unable to send an email to %s' % recipient)


def __create_message(to: str, days: int, uuid: str):
    message = EmailMessage()
    message.set_content(MAIL_CONTENT % (FEEDBACK_FORM_URL, uuid))
    message['Subject'] = MAIL_SUBJECT % days
    message['From'] = GMAIL_USERNAME
    message['To'] = to
    return message


def __create_message(subject: str, content: str, sender: str, recipient: str):
    message = EmailMessage()
    message.set_content(content)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient
    return message
