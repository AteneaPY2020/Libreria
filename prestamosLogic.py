from logic import Logic
from prestamosObj import prestamosObj
import os

class prestamosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "id_usuario",
            "id_libro",
            "fecha_prestamo",
            "fecha_entrega",
        ]