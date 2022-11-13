from flask import Flask
import datetime
from time import localtime

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.datetime.now()
    lt = localtime()
    tz = int(lt.tm_gmtoff/(60*60))

    iso = today.isoformat()
    dat = iso[:-7]

    if tz < 0:
        dat += '-'
    else: 
        dat += '+'
    
    if tz < 10: 
        dat += '0'

    dat += str(tz) + ':00'

    return dat

if __name__ == "__main__":
    app.run()
