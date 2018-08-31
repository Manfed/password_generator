import logging
from datetime import datetime, timedelta
from time import tzname

from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from password_generator.email.email_service.gmail_service import send_test_mail, send_mail
from password_generator.utils.constants import TEST_SCHEDULED_MAIL_SUBJECT, TEST_SCHEDULED_MAIL_CONTENT, \
    GENERATOR_FEEDBACK_FORM, GMAIL_USERNAME

__jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///../generator.db')
}
__executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
__job_defaults = {
    'coalesce': False,
    'max_instances': 3,
    'misfire_grace_time': 15 * 60
}
__scheduler = BackgroundScheduler(jobstores=__jobstores, executors=__executors,
                                  job_defaults=__job_defaults, timezone=utc,)


def init_scheduler():
    __scheduler.start()


def schedule_test(email: str, uuid: str, random_words_password: str, song_password: str):
    logger = logging.getLogger('scheduler')
    current_time = datetime.now()
    if not __scheduler.running:
        init_scheduler()

    first_mail_content = TEST_SCHEDULED_MAIL_CONTENT % (GENERATOR_FEEDBACK_FORM,
                                                        __create_password_tip(random_words_password),
                                                        __create_password_tip(song_password))
    send_mail(TEST_SCHEDULED_MAIL_SUBJECT, first_mail_content,
              GMAIL_USERNAME, email)

    logger.info('Scheduling job at {:%Y-%m-%d %H:%M:%S} %s'.format(current_time, tzname[0]))
    __scheduler.add_job(send_test_mail, 'date', run_date=current_time + timedelta(days=1),
                        timezone=tzname[0], args=[email, uuid, 1])
    __scheduler.add_job(send_test_mail, 'date', run_date=current_time + timedelta(days=3),
                        timezone=tzname[0], args=[email, uuid, 3])
    __scheduler.add_job(send_test_mail, 'date', run_date=current_time + timedelta(days=7),
                        timezone=tzname[0], args=[email, uuid, 7])


def __create_password_tip(password: str):
    return password[0:3] + (len(password[3:-3]) * '*') + password[-3:]
