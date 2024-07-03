from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES

db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    configure_uploads(app, photos)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
