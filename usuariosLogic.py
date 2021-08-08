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


    def count(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_usuario) FROM biblioteca.usuarios  "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        #data = self.lis(data, self.keys)
        
        return data