from flask import Flask

app = Flask(__name__)

from myproject.web import views
