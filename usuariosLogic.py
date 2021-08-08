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
            "usuario",
        ]
        
    #Insert usuario
    def insertUsuario(self, nombre, apellidos, correo, usuario):
        database = self.get_databaseXObj()
        sql = (
            "insert into biblioteca.usuarios (id_usuario, nombre, apellidos, correo, usuario) "
            + "values (0, %s, %s, %s, %s);"
        )
        data = (
            nombre,
            apellidos,
            correo,
            usuario,
        )
        rows = database.executeNonQueryRowsTuple(sql,data)
        return rows
    
    #Select Usuarios
    def getAllUsuarios(self):
        dataBase = self.get_databaseXObj()
        sql = "select * from biblioteca.usuarios;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    #Delete usuarios
    def deleteUsuarios(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from biblioteca.usuarios where usuarios.id_usuario = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def count(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_usuario) FROM biblioteca.usuarios  "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        #data = self.lis(data, self.keys)
        
        return data
