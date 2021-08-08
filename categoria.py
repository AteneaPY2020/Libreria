from flask import Blueprint, render_template, request, redirect, session
from categoriaLogic import categoriaLogic
from categoriaObj import categoriaObj

categoria = Blueprint(
    "categoria", __name__, template_folder="Templates", static_folder="static"
)

@categoria.route("/categoryIn", methods=["GET", "POST"])
def Insertcategory():
    try:
        logic = categoriaLogic()
        message = ""
        if request.method == "POST":
            categoria = request.form["categoria"]
            codigo = request.form["codigo"]
            #INSERTAR 
            formId = int(request.form["formId"])
            if formId == 1:
                rows = logic.insertCategory(categoria, codigo)
                message = "Se ha agregado una categoria"
                return render_template("category.html")
        elif request.method == "GET":
            return render_template("category.html")    
        
    except KeyError:
        return render_template(
            "index.html", messageSS="Su sesión ha expirado, ingrese nuevamente"
        )

@categoria.route("/listcategory", methods=["GET", "POST"])
def listcategory():
    try:
        logic = categoriaLogic()
        message = ""
        if request.method == "GET":
            data = logic.getAllCategory()
            return render_template("listcategory.html", data=data,)

        elif request.method == "POST":
            formId = int(request.form["formId"])
            #DELETE 
            if formId == 2:
                id_category = int(request.form["id"])
                logic.deleteCategory(id_category)
                message = "Se ha agregado una categoria"
                data = logic.getAllCategory()
                return render_template("listcategory.html", data=data,)
    except KeyError:
        return render_template(
            "index.html", messageSS="Su sesión ha expirado, ingrese nuevamente"
        )