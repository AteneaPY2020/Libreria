<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, session, Blueprint
from flask.scaffold import F
from nuevoPrestamo import nuevo_prestamo_blueprint
from prestamos import prestamo_blueprint
from prestamosPendientes import prestamos_pendientes_blueprint


app = Flask(__name__)
app.register_blueprint  (nuevo_prestamo_blueprint, url_prefix="")
app.register_blueprint(prestamo_blueprint, url_prefix="")
app.register_blueprint(prestamos_pendientes_blueprint, url_prefix="")
=======
from flask import Flask, render_template, request, redirect, session
from categoria import categoria
from usuarios import usuarios



app = Flask(__name__)
app.register_blueprint(categoria, url_prefix="")
app.register_blueprint(usuarios, url_prefix="")
#app.register_blueprint(inicio_inversionista, url_prefix="")
>>>>>>> Melanie
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
