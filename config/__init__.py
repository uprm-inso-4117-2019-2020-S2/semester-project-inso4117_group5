import os
from flask import Flask
from flask_cors import CORS

# Apply CORS to this app
template_dir = "../templates"
static_dir = "../static"
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = '5791628bb0b13ce0c676dfde280ba245'
app.config['JSON_SORT_KEYS'] = False  # This makes jsonify NOT sort automatically.
CORS(app)
