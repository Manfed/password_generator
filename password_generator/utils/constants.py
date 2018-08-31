import os

ROOT_DIR = os.path.dirname(__file__)
ROOT_DIR_ENV = os.getenv('DATABASE_FILE')

DATABASE_INIT_FILE_RELATIVE_PATH = '/../../words.txt'

if ROOT_DIR_ENV:
    DATABASE_INIT_FILE_PATH = ROOT_DIR_ENV
else:
    DATABASE_INIT_FILE_PATH = ROOT_DIR + DATABASE_INIT_FILE_RELATIVE_PATH

CHANGE_LETTER_SIZE_CHANCE_IN_PERCENT = 50

# Used to count the time to crack the password. Estimated rate of cracking password tries -> tries per second.
PASSWORD_CRACK_TRIES_PER_SECOND = 1e9

LATIN_CAPITAL_LETTERS = '[ABCDEFGHIJKLMNOPRSTUVWQXYZ]'
LATIN_SMALL_LETTERS = '[abcdefghijklmnoprstuvwqxyz]'
POLISH_CAPITAL_LETTERS = '[ĄĆĘŁŃŚÓŻŹ]'
POLISH_SMALL_LETTERS = '[ąćęłńśóżź]'
DIGITS = '[0123456789]'
SPECIAL_CHARACTERS = '[!@#$%^&*()-=+_;:\'"/\,.<>[\]{}]'

MINIMAL_RANDOM_WORD_LENGTH = 3

# E-mail account settings
GMAIL_USERNAME = 'pg.master.thesis.pass.gen@gmail.com'
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
FEEDBACK_FORM_URL = 'https://www.surveygizmo.com/s3/4541212/Badanie-stopnia-zapami-tania-has-a-stworzonego-przy-u-yciu-generatora-hase'
MAIL_SUBJECT = 'Check how do you remember passwords after %d day(s)'
MAIL_CONTENT = """
    Hi,
    thank you for participating in the study of the possibility of memorizing passwords.
    Here you can find the form with the questions checking your password memory: %s.
    
    Your ID is: %s
    
    Cheers!
"""

GENERATOR_FEEDBACK_FORM = 'https://www.surveygizmo.com/s3/4541048/Badanie-zadowolenia-u-ytkownik-w-z-u-ywania-generatora-hase'
TEST_SCHEDULED_MAIL_SUBJECT = 'Thank you for participating in the studies.'
TEST_SCHEDULED_MAIL_CONTENT = """
    Hello,
    thank you for participating in the study of the possibility of memorizing password.
    
    If you didn't fill the survey about impressions from using the password generator, please fill it in now.
    You can find it here: %s
    
    Cheers!
    
    PS Here you have small tips regarding your passwords:
    Password created from random words: %s
    Password created from song's verse: %s
"""
