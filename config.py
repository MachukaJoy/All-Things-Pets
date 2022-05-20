import os

class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
  
class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql://keqquleglptiww:4e8db2a70c9ad2d1fc08b9ab11f82dcbb02a3c4bb1d30451de9479bcdc97ab07@ec2-34-201-95-176.compute-1.amazonaws.com:5432/d6ev25njuahra7'

class DevConfig(Config):
  #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:oa2exWako@localhost/pets'


  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 