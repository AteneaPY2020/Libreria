from logic import Logic
from administradorObj import administradorObj
import os


class administradorLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "usuario",
            "contrasenna",
            "correo",
            "nombre",
        ]