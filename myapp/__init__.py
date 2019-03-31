from flask import Flask
from myapp import routes
from flask_script import Manager
from .routes import app
from flask_cors import CORS
CORS(app, supports_credentials=True)

if __name__ == '__main__':

    manager = Manager(app)
    manager.run()