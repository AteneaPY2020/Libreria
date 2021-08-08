from flask import Blueprint, render_template, request, redirect, session
from usuariosLogic import usuariosLogic
from usuariosObj import usuariosObj

usuarios = Blueprint(
    "usuarios", __name__, template_folder="Templates", static_folder="static"
)

@usuarios.route("/userIn", methods=["GET", "POST"])
def InsertUsuario():
    try:
        logic = usuariosLogic()
        message = ""
        if request.method == "POST":
            nombre = request.form["nombre"]
            apellidos = request.form["apellidos"]
            correo = request.form["correo"]
            usuario = request.form["usuario"]
            #INSERTAR 
            formId = int(request.form["formId"])
            if formId == 1:
                rows = logic.insertUsuario(nombre, apellidos, correo,usuario)
                message = "Se ha agregado un usuario"
                return render_template("student.html")
        elif request.method == "GET":
            return render_template("student.html")    
        
    except KeyError:
        return render_template(
            "index.html", messageSS="Su sesión ha expirado, ingrese nuevamente"
        )

@usuarios.route("/liststudent", methods=["GET", "POST"])
def listcategory():
    try:
        logic = usuariosLogic()
        message = ""
        if request.method == "GET":
            data = logic.getAllUsuarios()
            return render_template("liststudent.html", data=data,)

        elif request.method == "POST":
            formId = int(request.form["formId"])
            #DELETE 
            if formId == 2:
                id_user = int(request.form["id"])
                logic.deleteUsuarios(id_user)
                message = "Se ha agregado un usuario"
                data = logic.getAllUsuarios()
                return render_template("liststudent.html", data=data,)
    except KeyError:
        return render_template(
            "index.html", messageSS="Su sesión ha expirado, ingrese nuevamente"
        )