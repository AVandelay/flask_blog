import os

# SECRET_KEY = 'you-will-never-guess'
# DEBUG=True
# DB_USERNAME = 'avandelay'
# DB_PASSWORD = '' # not required for cloud9
# BLOG_DATABASE_NAME = 'blog'
# DB_HOST = os.getenv('IP', '0.0.0.0')
# DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
# SQLALCHEMY_DATABASE_URI = DB_URI
# UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
# UPLOADED_IMAGES_URL = '/static/images/'

SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'root'
DB_PASSWORD = 'test'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = 'mysql:3306'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
UPLOADED_IMAGES_DEST = '/opt/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
