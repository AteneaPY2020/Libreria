from logic import Logic
from librosObj import librosObj
import os


class librosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "titulo",
            "autor",
            "edicion",
            "editorial",
            "sinopsis",
            "portada",
            "portada_nombre",
            "correlativo",
            "pais",
            "anno",
            "ejemplares",
            "disponibles",
            "id_categoria",
        ]