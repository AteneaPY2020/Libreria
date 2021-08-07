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

    def getAllprestamosTot(self):
            dataBase = self.get_databaseXObj()
            sql = (
                "select prestamos.id_prestamo, libros.id_libro, libros.titulo, libros.disponibles, usuarios.usuario, prestamos.fecha_prestamo, prestamos.fecha_entrega "
                + "from biblioteca.libros inner join biblioteca.prestamos on libros.id_libro = prestamos.id_libro "
                + "inner join biblioteca.usuarios on prestamos.id_usuario = usuarios.id_usuario "
                + "where prestamos.entregado = 1 order by prestamos.fecha_entrega;"
            )
            data = dataBase.executeQuery(sql)
            data = self.tupleToDictionaryList(
                data, ["id_prestamo", "id_usuario","titulo", "id_libro", "usuario","fecha_prestamo","fecha_entrega"]
            )
            return data

    def newPrestamo(self, id_libro, id_usuario, fecha_prestamo, fecha_devolucion, disponibles):
        dataBase = self.get_databaseXObj()
        sql = (
            "insert into biblioteca.prestamos (id_prestamo, id_libro, id_usuario, fecha_prestamo, fecha_entrega) "
            + f"values (0, {id_libro}, {id_usuario}, '{fecha_prestamo}', '{fecha_devolucion}');"
        )
        rows = dataBase.executeNonQueryRows(sql)

        self.updateDisponible(id_libro, disponibles)

        return rows

    def getAllPrestamosPendientes(self):
            dataBase = self.get_databaseXObj()
            sql = (
                "select prestamos.id_prestamo, libros.id_libro, libros.titulo, libros.disponibles, usuarios.usuario, prestamos.fecha_prestamo, prestamos.fecha_entrega "
                + "from biblioteca.libros inner join biblioteca.prestamos on libros.id_libro = prestamos.id_libro "
                + "inner join biblioteca.usuarios on prestamos.id_usuario = usuarios.id_usuario "
                + "where prestamos.entregado = 0 order by prestamos.fecha_entrega;"
            )
            data = dataBase.executeQuery(sql)
            data = self.tupleToDictionaryList(
                data, ["id_prestamos", "id_libro","titulo", "disponibles","usuario", "fecha_prestamo", "fecha_entrega"]
            )
            return data

    def updatePrestamoSatus(self, id_prestamo, id_libro, disponibles):
        dataBase = self.get_databaseXObj()

        sql = (
            "UPDATE biblioteca.prestamos set prestamos.entregado = 1 "
            + f"where prestamos.id_prestamo = {id_prestamo}"
        )

        rows = dataBase.executeNonQueryRows(sql)
        self.updateDisponible(id_libro, disponibles)
        
        return rows

    def updateDisponible(self, id_libro, disponibles):
        dataBase = self.get_databaseXObj()

        sql = (
            "UPDATE biblioteca.libros set disponibles = %s "
            + "where id_libro = %s;"
        )

        data = (disponibles, id_libro)
        rows = dataBase.executeNonQueryRowsTuple(sql, data)
        
        return rows