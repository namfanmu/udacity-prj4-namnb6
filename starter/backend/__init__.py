import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Start app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
    )
