import os

class Config:
    SECRET_KEY ='4486af1672cae8e6b97cd49b0368c96a'
    SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    MAIL_USE_TLS = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_PORT = 587