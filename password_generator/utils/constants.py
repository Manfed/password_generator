import os

ROOT_DIR = os.path.dirname(__file__)
ROOT_DIR_ENV = os.getenv('DATABASE_FILE')

DATABASE_INIT_FILE_RELATIVE_PATH = '/../../words.txt'

if ROOT_DIR_ENV:
    DATABASE_INIT_FILE_PATH = ROOT_DIR_ENV
else:
    DATABASE_INIT_FILE_PATH = ROOT_DIR + DATABASE_INIT_FILE_RELATIVE_PATH

CHANGE_LETTER_SIZE_CHANCE_IN_PERCENT = 50

LATIN_CAPITAL_LETTERS = '[ABCDEFGHIJKLMNOPRSTUVWQXYZ]'
LATIN_SMALL_LETTERS = '[abcdefghijklmnoprstuvwqxyz]'
POLISH_CAPITAL_LETTERS = '[ĄĆĘŁŃŚÓŻŹ]'
POLISH_SMALL_LETTERS = '[ąćęłńśóżź]'
DIGITS = '[0123456789]'
SPECIAL_CHARACTERS = '[!@#$%^&*()-=+_;:\'"/\,.<>[\]{}]'

# E-mail account settings
GMAIL_USERNAME = 'pg.master.thesis.pass.gen@gmail.com'
GMAIL_PASSWORD = 'M@rcln1!'
FEEDBACK_FORM_URL = 'https://goo.gl/forms/W6wB9cbW12V1DeOo1'
MAIL_SUBJECT = 'Check how do you remember passwords after %d day(s)'
MAIL_CONTENT = """
    Hi,
    thank you for participating in the study of the possibility of memorizing passwords.
    Here you can find the form with the questions checking your password memory: %s.
    
    Your ID is: %s
    
    Cheers!
"""
