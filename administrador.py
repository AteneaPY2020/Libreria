from flask import Blueprint, Flask, render_template, request, redirect
from logic import Logic
import mysql.connector
from mysql.connector import Error
from administradorLogic import administradorLogic
from administradorObj import administradorObj

admin_blueprint = Blueprint(
    "administradores", __name__, template_folder="Templates", static_folder="static"
)

@admin_blueprint.route("/admin")
def admin():
    return render_template("admin.html")

@admin_blueprint.route("/listadmin", methods=["GET", "POST"])
def listadmin():
    if request.method == "GET":
        logic = administradorLogic
        data = logic().getAllAdmin()
        return render_template("listadmin.html", data = data)
    
@admin_blueprint.route("/admininsert", methods=["GET", "POST"])
def admininsert():
    logic = administradorLogic()
    message = ""
    verdadero = False
    if request.method == "GET":
        data = logic.getAllAdmin()
        return render_template("listadmin.html", data=data, message=message)
    if request.method == "POST":
        formId = int(request.form["formId"])
        # INSERTAR
        if formId == 1:
            logic = administradorLogic()
            usuario= (request.form["usuario"])
            contrasenna= (request.form["contrasenna"])
            correo = (request.form["correo"])
            nombre= (request.form["nombre"])
            # Comprobando si existe
            existeUsuario = logic.checkUserInAdmin(usuario)

            if not existeUsuario:
                rows = logic.insertAdmin (usuario,contrasenna,correo,nombre )
                data = logic.getAllAdmin()
                message = "Se ha agregado un nuevo administrador"
                return render_template(
                    "admin.html", data=data, message=message
                )
            else:
                data = logic.getAllAdmin()
                message = "El usuario ya existe, pruebe otro"
                return render_template(
                    "admin.html", data=data, message=message
                )
        # ELIMINAR
        elif formId == 2:
            id_administrador = int(request.form["id"])
            logicDelete = administradorLogic()
            logicDelete.deleteAdmin(id_administrador)
            message2 = "Se ha eliminado un administrador"
            data = logic.getAllAdmin()
            return render_template("listadmin.html", data=data, message2=message2)
