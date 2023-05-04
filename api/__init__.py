from flask import Flask
from flask_cors import CORS
from .config import config
import os 


APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')


def create_app(config_name="default"):
    app = Flask(__name__,template_folder=TEMPLATE_PATH)

    # App Configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Allow cors
    CORS(app)

    CORS(app, resources={

        r"/*":{
        "origins":"*"
        }
    })

    from .main import qa_transcript_pb
    app.register_blueprint(qa_transcript_pb)

    return app