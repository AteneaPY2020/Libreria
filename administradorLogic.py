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
    #Obtener todos los admin
    def getAllAdmin(self):
        dataBase = self.get_databaseXObj()
        sql = f"select * from biblioteca.administradores;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    #Insertar un admin
    def insertAdmin(self, usuario, contrasenna, correo, nombre ):
        database = self.get_databaseXObj()
        sql = f"insert into biblioteca.administradores (usuario, contrasenna, correo, nombre) values ('{usuario}','{contrasenna}','{correo}', '{nombre}');"
        rows = database.executeNonQueryRows(sql)
        return rows
    #Delete un admin
    def deleteAdmin(self, id_administrador):
        database = self.get_databaseXObj()
        sql = "delete from biblioteca.administradores " + f"where id_administrador = {id_administrador};"
        print(sql)
        rows = database.executeNonQueryRows(sql)
        return rows
    
    #Check si ya existe un admin 
    def checkUserInAdmin(self, usuario):
        dataBase = self.get_databaseXObj()
        sql = (
            "SELECT administradores.usuario FROM biblioteca.administradores "
            + f"where administradores.usuario = '{usuario}';"
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        counter = 0
        for item in data:
            counter += 1

        if counter > 0:
            return True
        else:
            return False