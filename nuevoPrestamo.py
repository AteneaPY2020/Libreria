from flask import Blueprint, render_template, request, redirect, session
import os
from prestamosLogic import prestamosLogic
from prestamosObj import prestamosObj


nuevo_prestamo_blueprint = Blueprint(
    "nuevo_prestamo", __name__, template_folder="Templates", static_folder="static"
)

@nuevo_prestamo_blueprint.route("/nuevoPrestamo", methods=["GET", "POST"])
def nuevo_prestamo():
    error = False
    if request.method == "GET":
        # Recoge las listas necesarios
        libros = prestamosLogic().getAllLibrosCodigos()
        usuarios = prestamosLogic().getAllUsuarios()
        return render_template("newloan.html", libros=libros, usuarios=usuarios)
    
    elif request.method == "POST":
        libro = request.form["libro"]
        usuario = request.form["usuario"]
        fecha_prestamo = request.form["fecha_prestamo"]
        fecha_devolucion = request.form["fecha_devolucion"]

        listaLibro = libro.split()
        id_libro = int(listaLibro[0])
        disponibles = int(listaLibro[1]) - 1
        
        # Recoge las listas necesarios
        libros = prestamosLogic().getAllLibrosCodigos()
        usuarios = prestamosLogic().getAllUsuarios()

        if disponibles + 1 == 0:
            message = "No hay libros disponibles. No se puede realizar el prestamo"
            error = True
            return render_template("newloan.html", libros=libros, usuarios=usuarios, message=message, error=error)
        else:
            prestamosLogic().newPrestamo(id_libro, usuario, fecha_prestamo, fecha_devolucion, disponibles) 
            return render_template("newloan.html", libros=libros, usuarios=usuarios)