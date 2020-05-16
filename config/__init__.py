from flask import Flask
from flask_cors import CORS

# Apply CORS to this app
app = Flask(__name__)
app.secret_key = '5791628bb0b13ce0c676dfde280ba245'
app.config['JSON_SORT_KEYS'] = False  # This makes jsonify NOT sort automatically.
CORS(app)
