from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from celery import Celery
from flask_mail import Mail
from redis import Redis
from flask_cors import CORS
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    CORS(app)

    with app.app_context():
        from .routes.admin_routes import bp as admin_bp
        from .routes.auth_routes import bp as auth_bp
        from .routes.sponsor_routes import bp as sponsor_bp
        from .routes.influencer_routes import bp as influencer_bp

        app.register_blueprint(admin_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(sponsor_bp)
        app.register_blueprint(influencer_bp)

        create_admin_if_not_exists()


    return app

def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery

def create_admin_if_not_exists():
    from app.models import User
    admin_email = 'deepanshupathak03@gmail.com'
    admin_username = 'deepanshu'
    admin_password = 'deepanshu123'

    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(
            username=admin_username,
            email=admin_email,
            password_hash=generate_password_hash(admin_password),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user created with email: {admin_email} and password: {admin_password}")
    else:
        print("Admin user already exists")