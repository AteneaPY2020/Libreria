from logic import Logic
from prestamosObj import prestamosObj
import os

class prestamosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "id_usuario",
            "id_libro",
            "fecha_prestamo",
            "fecha_entrega",
        ]

    def count(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_prestamo) FROM biblioteca.prestamos WHERE entregado ='1' "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        #data = self.lis(data, self.keys)
        
        return data

    def count_pendiente(self):
        dataBase = self.get_databaseXObj()
        sql = (
            " SELECT COUNT(id_prestamo) FROM biblioteca.prestamos WHERE entregado ='0' "
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        #data = self.lis(data, self.keys)
        
        return data

        