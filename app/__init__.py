from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config_options


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view  = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # config_options[config_name].init_app(app)
    

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    # configure UploadSet

    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as authentication_blueprint
    app.register_blueprint(authentication_blueprint)
    
    return app 
