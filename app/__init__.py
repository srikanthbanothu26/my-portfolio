from flask import Flask
from app.scripts.scripts import script_bp


app = Flask(__name__)
app.register_blueprint(script_bp)
