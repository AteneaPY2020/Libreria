from flask import Blueprint, render_template, request, redirect, session
from administradorLogic import administradorLogic
from administradorObj import administradorObj
from usuariosLogic import usuariosLogic
from usuariosObj import usuariosObj
from librosLogic import librosLogic
from librosObj import librosObj
from categoriaLogic import categoriaLogic
from categoriaObj import categoriaObj

from prestamosLogic import prestamosLogic
from prestamosObj import prestamosObj
import os

home_blueprint = Blueprint(
    "home", __name__, template_folder="Templates", static_folder="static"
)

@home_blueprint.route("/home", methods=["GET", "POST"])
def countHome():
    if request.method == "GET":
        #LOGICS
        admin_logic = administradorLogic()
        usuario_logic = usuariosLogic()
        libros_logic = librosLogic()
        categoria_logic = categoriaLogic()
        loan_logic = prestamosLogic()
        
        #COUNTS
        admin_count = admin_logic.count()
        usuarios_count = usuario_logic.count()
        libros_count = libros_logic.count()
        categoria_count = categoria_logic.count()
        prestamos_count = loan_logic.count()
        prestamos_count_pendiente = loan_logic.count_pendiente()


        return render_template("home.html", admin_count=admin_count, usuarios_count=usuarios_count,
        libros_count=libros_count, categoria_count=categoria_count,prestamos_count=prestamos_count,
        prestamos_count_pendiente=prestamos_count_pendiente,)

