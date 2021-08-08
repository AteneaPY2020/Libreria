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


    def getUser(self, usuario, contrasenna):
            dataBase = self.get_databaseXObj()
            sql = (
                "SELECT * FROM biblioteca.administradores "
                + f"where administradores.usuario = '{usuario}' and administradores.contrasenna = '{contrasenna}';"
            )
            print(sql)
            data = dataBase.executeQuery(sql)
            data = self.tupleToDictionaryList(data, self.keys)
            
            
            return data

    def createDictionary(self, adminObj):
        dictionary = {
            "id": adminObj.id,
            "usuario": adminObj.user,
            "contrasenna": adminObj.password,
        }
        return dictionary

    
    
    
    def countAdmin(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_administrador) FROM biblioteca.administradores  "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        
        return data