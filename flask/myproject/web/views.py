from flask import render_template

from myproject.web import app

@app.route('/')
def home():
    return render_template("home.html")
