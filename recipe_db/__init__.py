from flask import Flask
import os

# create and configure the app
def create_app(app_environment=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='db.sqlite',
    )

    if app_environment == 'production':
        app = Flask(__name__)
        app.config.from_envvar('PROD_ENV')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__== "__main__":
    app = create_app(os.getenv('FLASK_ENV', 'dev'))
