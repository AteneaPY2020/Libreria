from logic import Logic
from categoriaObj import categoriaObj
import os


class categoriaLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "categoria",
            "codigo",
        ]