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
            "correlativo",
            "pais",
            "anno",
            "disponibles",
            "id_categoria",
        ]

    def getAllLibros(self):
        dataBase = self.get_databaseXObj()
        sql = "SELECT * FROM biblioteca.libros;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data
    
    def insertLibro(self, titulo,autor,edicion, editorial, correlativo, pais, anno, disponibles, id_categoria ):
        database = self.get_databaseXObj()
        sql = f"insert into biblioteca.libros (titulo,autor,edicion, editorial, correlativo, pais, anno, disponibles, id_categoria) values ('{titulo}','{autor}','{edicion}', '{editorial}', '{correlativo}', '{pais}', '{anno}', {disponibles}, {id_categoria});"
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteAdmin(self, id_libros):
        database = self.get_databaseXObj()
        sql = "delete from biblioteca.libros " + f"where id_libro = {id_libros};"
        rows = database.executeNonQueryRows(sql)
        return rows