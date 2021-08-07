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

    #Insert category
    def insertCategory(self, categoria, codigo):
        database = self.get_databaseXObj()
        sql = (
            "insert into biblioteca.categoria (id_categoria, categoria, codigo) "
            + "values (0, %s, %s);"
        )
        data = (
            categoria,
            codigo,
        )
        rows = database.executeNonQueryRowsTuple(sql,data)
        return rows
    
    #Select Categoria
    def getAllCategory(self):
        dataBase = self.get_databaseXObj()
        sql = "select * from biblioteca.categoria;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    #Delete categoria
    def deleteCategory(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from biblioteca.categoria where categoria.id_categoria = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    #Get ID de categoria por nombre
    def getCategoryIDbyName(self,name):
        dataBase = self.get_databaseXObj()
        sql = "select id_categoria from biblioteca.categoria " + f"where categoria = {name};"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            categoriaObj = categoriaObj(
                data_dic["id"],
                data_dic["categoria"],
                data_dic["codigo"],
            )
            return categoriaObj
        else:
            return None