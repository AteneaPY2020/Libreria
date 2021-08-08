from flask import Flask, render_template, request, redirect, session
from administradorLogic import administradorLogic
from administrador import admin_blueprint

app = Flask(__name__)
app.register_blueprint(admin_blueprint, url_prefix="")
#app.register_blueprint(registro_productos, url_prefix="")
#app.register_blueprint(inicio_inversionista, url_prefix="")
#app.register_blueprint(emprendimiento, url_prefix="")
#app.register_blueprint(emprendimientoInicio, url_prefix="")
#app.register_blueprint(emprendedorProfile, url_prefix="")
#app.register_blueprint(cerrarSesion, url_prefix="")
#app.register_blueprint(admin, url_prefix="")
app.secret_key = "ILoveFishing"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
