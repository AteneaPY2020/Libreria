from logic import Logic
from usuariosObj import usuariosObj
import os


class usuariosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre",
            "apellidos",
            "correo",
        ]