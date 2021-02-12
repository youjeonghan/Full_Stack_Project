from flask import Flask
from view import bp

app = Flask(__name__)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)