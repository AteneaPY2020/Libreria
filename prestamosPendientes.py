from flask import Blueprint, render_template, request, redirect, session
import os
from prestamosLogic import prestamosLogic
from prestamosObj import prestamosObj

prestamos_pendientes_blueprint = Blueprint(
    "prestamos_pendientes", __name__, template_folder="Templates", static_folder="static"
)

@prestamos_pendientes_blueprint.route("/prestamosPendientes", methods=["GET", "POST"])
def nuevo_prestamo():
    if request.method == "GET":
        prestamos = prestamosLogic().getAllPrestamosPendientes()
        return render_template("loanpending.html", prestamos=prestamos)
    
    elif request.method == "POST":
        id_prestamo = request.form["id_prestamo"]
        id_libro = request.form["id_libro"]
        disponibles = int(request.form["disponibles"]) + 1
        prestamosLogic().updatePrestamoSatus(id_prestamo, id_libro, disponibles)

        prestamos = prestamosLogic().getAllPrestamosPendientes()
        return render_template("loanpending.html", prestamos=prestamos)