from flask import Blueprint, render_template, request, redirect, session
from administradorLogic import administradorLogic
from administradorObj import administradorObj
import os

login_admin_blueprint = Blueprint(
    "login_admin", __name__, template_folder="Templates", static_folder="static"
)

@login_admin_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html", message="")
    elif request.method == "POST":
        usuario = request.form["usuario"]
        contrasenna = request.form["contrasenna"]
        logic = administradorLogic()
        userData = logic.getUser(usuario, contrasenna)

        if userData is not None:
            dataDic = logic.createDictionary(userData)
            session["user"] = dataDic
            return redirect("/home")
        else:
            return render_template(
                "index.html", message="Error. Usuario o contraseña incorrecta"
            )


#@home.route("/home", methods=["GET", "POST"])
#def home():
#    try:
#        user = session["user"]
#        usuario = user["usuario"]
#        return render_template("home.html", usuario=usuario)
#    except KeyError:
#        return render_template(
#            "index.html", messageSS="Su sesión ha expirado, ingrese nuevamente"
#        )

