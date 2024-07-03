class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'uploads'
