from flask import Blueprint, render_template, request, redirect, session
import os
from prestamosLogic import prestamosLogic
from prestamosObj import prestamosObj

prestamo_blueprint = Blueprint(
    "prestamo", __name__, template_folder="Templates", static_folder="static"
)

@prestamo_blueprint.route("/prestamos", methods=["GET", "POST"])
def nuevo_prestamo():
    return render_template("loan.html")