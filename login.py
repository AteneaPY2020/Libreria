from flask import Blueprint, render_template, request, redirect, session
from administradorLogic import administradorLogic
from administradorObj import administradorObj
import os

login_admin = Blueprint(
    "login", __name__, template_folder="Templates", static_folder="static"
)

@login_admin.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html", message="")
    elif request.method == "POST":
        usuario = request.form["usuario"]
        contrasenna = request.form["contrasenna"]
        logic = administradorLogic()
        userData = logic.getUser(usuario, contrasenna)

        if userData is not None:
            
            session["user"] = userData
            return render_template("home.html")
        else:
            return render_template(
                "index.html", message="Error. Usuario o contraseña incorrecta"
            )

