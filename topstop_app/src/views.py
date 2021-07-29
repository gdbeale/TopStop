from datetime import datetime
from flask import Flask, render_template
from flask.templating import Environment
from .. import app
from ..src.nextrip import NexTrip
from ..src.topstop import TopStopRequest


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/topstop/")
def topstop():
    routes = NexTrip().get_routes()
    return render_template("topstop.html", routes=routes)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
