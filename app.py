from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "subdomain takeover POC by maskop9(mas_kop9@protonmail.com)"
