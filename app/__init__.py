from flask import Flask
from config import *
import os

# create and configure the app
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='db.sqlite',
    )

    if test_config is None:
        # load the normal "dev" config
        app.config.from_object('config.Config')
    else:
        # load the "test" config
        app.config.from_object('config.TestConfig')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__== "__main__":
    app = create_app()
