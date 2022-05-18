# from email.policy import default
import os
# from decouple import config


class Config:

    SECRET_KEY = '123QWERTY'


class ProdConfig(Config):
    DEBUG = True


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
