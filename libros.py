from flask import Blueprint, render_template, request, redirect, session
from logic import Logic
from librosObj import librosObj
from librosLogic import librosLogic

libros_blueprint = Blueprint(
    "libros", __name__, template_folder="Templates", static_folder="static"
)
@libros_blueprint.route("/book")
def book():
    return render_template("book.html")

@libros_blueprint.route("/catalog", methods=["GET", "POST"])
def catalog():
    if request.method == "GET":
        logic = librosLogic
        libros = logic().getAllLibros()
    return render_template(
            "catalog.html", data = libros
        )
@libros_blueprint.route("/bookinsert", methods=["GET", "POST"])
def bookinsert():
    if request.method == "POST":
        logic = librosLogic()
        titulo= (request.form["titulo"])
        autor= (request.form["autor"])
        edicion = (request.form["edicion"])
        editorial= (request.form["editorial"])
        correlativo= (request.form["correlativo"])
        pais= (request.form["pais"])
        anno= (request.form["anno"])
        disponibles= int((request.form["disponibles"]))
        logic.insertLibro (titulo,autor,edicion, editorial, correlativo, pais, anno, disponibles, 1 )
    return render_template(
            "book.html", message = "Insertado correctamente"
        )