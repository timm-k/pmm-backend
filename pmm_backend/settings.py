# flask core settings
DEBUG = True
TESTING = True
SECRET_KEY = "ABC"  # CHANGE ME

# database settings
SQLALCHEMY_DATABASE_URI = 'mysql://pmm:jACjdfdxWbYL5@git.timakramo.de:3306/pmmtest'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'