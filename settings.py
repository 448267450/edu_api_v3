class Dev():
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rwk2011416031@47.117.48.128/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATION = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True