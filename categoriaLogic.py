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

    def count(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_categoria) FROM biblioteca.categoria  "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        #data = self.lis(data, self.keys)
        
        return data