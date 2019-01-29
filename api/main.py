from flask import Flask
import models
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "<h1> Hello </h1>"

if __name__ == "__main__":
    print("Initializing database")
    models.init_db()
    print("Running app")
    app.run(host='0.0.0.0', port=80)


