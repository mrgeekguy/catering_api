from flask import Flask
from models import db
# import bcrypt when ready
# controllers import jwt, auth, event_control

# App instance
app = Flask(__name__)

# Configuration style setup
app.config.from_object("config.Development")

db.init_app(app)

if __name__ == "__main__":
    app.run() # do not use in deployment environment
