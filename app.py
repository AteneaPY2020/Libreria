from flask import Flask, render_template, request, redirect, session, Blueprint
from flask.scaffold import F
from nuevoPrestamo import nuevo_prestamo_blueprint
from prestamos import prestamo_blueprint
from prestamosPendientes import prestamos_pendientes_blueprint
from categoria import categoria
from usuarios import usuarios
from libros import libros_blueprint
from administrador import admin_blueprint
from login import login_admin
from home import home_blueprint


app = Flask(__name__)
app.register_blueprint(admin_blueprint, url_prefix="")
app.register_blueprint(categoria, url_prefix="")
app.register_blueprint(usuarios, url_prefix="")
app.register_blueprint(nuevo_prestamo_blueprint, url_prefix="")
app.register_blueprint(prestamo_blueprint, url_prefix="")
app.register_blueprint(prestamos_pendientes_blueprint, url_prefix="")
app.register_blueprint(libros_blueprint, url_prefix="")
app.register_blueprint(login_admin, url_prefix="")
app.register_blueprint(home_blueprint, url_prefix="")
app.secret_key = "ILoveFishing"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
