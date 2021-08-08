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

    def count(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_libro) FROM biblioteca.libros  "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        #data = self.lis(data, self.keys)
        
        return data