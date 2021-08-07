from flask import Blueprint, render_template, request, redirect, session
import os
from prestamosLogic import prestamosLogic
from prestamosObj import prestamosObj


nuevo_prestamo_blueprint = Blueprint(
    "nuevo_prestamo", __name__, template_folder="Templates", static_folder="static"
)

@nuevo_prestamo_blueprint.route("/nuevoPrestamo", methods=["GET", "POST"])
def nuevo_prestamo():
    if request.method == "GET":
        # Recoge las listas necesarios
        libros = prestamosLogic().getAllLibrosCodigos()
        usuarios = prestamosLogic().getAllUsuarios()
        return render_template("newloan.html", libros=libros, usuarios=usuarios)
    
    elif request.method == "POST":
        # Recoge las listas necesarios
        libros = prestamosLogic().getAllLibrosCodigos()
        usuarios = prestamosLogic().getAllUsuarios()

        libro = request.form["libro"]
        usuario = request.form["usuario"]
        fecha_prestamo = request.form["fecha_prestamo"]
        fecha_devolucion = request.form["fecha_devolucion"]

        listaLibro = libro.split()
        id_libro = int(listaLibro[0])
        disponibles = int(listaLibro[1]) - 1

        prestamosLogic().newPrestamo(id_libro, usuario, fecha_prestamo, fecha_devolucion, disponibles) 

        return render_template("newloan.html", libros=libros, usuarios=usuarios)