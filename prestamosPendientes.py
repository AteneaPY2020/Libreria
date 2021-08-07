from flask import Blueprint, render_template, request, redirect, session
import os
from prestamosLogic import prestamosLogic
from prestamosObj import prestamosObj

prestamos_pendientes_blueprint = Blueprint(
    "prestamos_pendientes", __name__, template_folder="Templates", static_folder="static"
)

@prestamos_pendientes_blueprint.route("/prestamosPendientes", methods=["GET", "POST"])
def nuevo_prestamo():
    return render_template("loanpending.html")