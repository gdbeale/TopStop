from flask import current_app as app
from flask import Flask, render_template, request, g
from flask.templating import Environment
from datetime import datetime
from ..src.nextrip import NexTrip
from ..src.topstop import TopStopRequest


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/topstop/")
def topstop():
    routes = NexTrip().get_routes()
    return render_template("topstop.html", routes=routes)


@app.route("/get_directions/", methods=['GET'])
def directions():
    topstop_req = TopStopRequest(request.request.args.get("route"))
    return render_template("topstop.html", topstop_req=topstop_req)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")
