from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345678'

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth,url_prefix = '/')

    return app