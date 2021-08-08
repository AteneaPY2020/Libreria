from flask import Blueprint, render_template, request, redirect, session
from administradorLogic import administradorLogic
from administradorObj import administradorObj
import os

home = Blueprint(
    "home", __name__, template_folder="Templates", static_folder="static"
)

@home.route("/home", methods=["GET", "POST"])
def countHome():
    logic = administradorLogic()
    if request.method == "GET":
        data = logic.countAdmin()
        return render_template("home.html", data=data,)

