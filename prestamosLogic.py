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

    def getAllLibrosCodigos(self):
            dataBase = self.get_databaseXObj()
            sql = (
                "select libros.id_libro, libros.correlativo, libros.titulo, libros.disponibles "
                + "from libros;"
            )
            data = dataBase.executeQuery(sql)
            data = self.tupleToDictionaryList(
                data, ["id_libro", "correlativo", "titulo", "disponibles"]
            )
            return data

    def getAllUsuarios(self):
            dataBase = self.get_databaseXObj()
            sql = (
                "select usuarios.id_usuario, usuarios.nombre, usuarios.apellidos, usuarios.correo  "
                + "from usuarios;"
            )
            data = dataBase.executeQuery(sql)
            data = self.tupleToDictionaryList(
                data, ["id_usuario", "nombre", "apellidos", "correo"]
            )
            return data

    def newPrestamo(self, id_libro, id_usuario, fecha_prestamo, fecha_devolucion, disponibles):
        dataBase = self.get_databaseXObj()
        sql = (
            "insert into biblioteca.prestamos (id_prestamo, id_libro, id_usuario, fecha_prestamo, fecha_entrega) "
            + f"values (0, {id_libro}, {id_usuario}, '{fecha_prestamo}', '{fecha_devolucion}');"
        )
        rows = dataBase.executeNonQueryRows(sql)

        sql2 = (
            "UPDATE biblioteca.libros set disponibles = %s "
            + "where id_libro = %s;"
        )

        data = (disponibles, id_libro)
        rows = dataBase.executeNonQueryRowsTuple(sql2, data)
        
        return rows