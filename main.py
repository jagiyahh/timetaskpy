from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.now()
    iso = today.isoformat()
    date = iso[:-7] + '+00:00'

    return date

if __name__ == "__main__":
    app.run()