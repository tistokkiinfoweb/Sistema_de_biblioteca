from flask import Flask, render_template, session as flask_session

app = Flask(__name__)

app.secret_key = "AdventureTime ep The Real You"

@app.route("/")
def index():
    return render_template('index.html')