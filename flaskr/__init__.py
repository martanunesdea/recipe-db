import os
from flask import Flask
from config import *

from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError


URI = 'mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db?retryWrites=true&w=majority'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.Config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

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
    #db_uri = "mongodb://'127.0.0.1:27017/mydatabase"
    app = create_app()
    #app.run("0.0.0.0", port=5000, debug=False)
