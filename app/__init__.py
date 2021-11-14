from flask import Flask
from flask_pymongo import PyMongo
from config import *

# create and configure the app
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the normal "dev" config
        app.config.from_object('config.Config')
    else:
        # load the "test" config
        app.config.from_object('config.TestConfig')

    #db.init_app(app)
    db = PyMongo(app, uri=app.config["URI"])

    from . import auth
    app.register_blueprint(auth.bp)

    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__== "__main__":
    app = create_app()
