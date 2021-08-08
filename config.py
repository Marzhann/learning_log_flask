import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'll.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'yy&aqtrvt$otp1p30sjyam7^!&j0jrvljr(9ci99aek5tx@+s8'
    