from flask import Flask, session
from flask.ext.session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

import routes

if __name__ == "__main__":
    app.run(port=5000)