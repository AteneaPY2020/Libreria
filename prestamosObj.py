class prestamosObj:
    def __init__(
        self,
        id,
        id_usuario,
        id_libro,
        fecha_prestamo,
        fecha_entrega,
    ):
        self.id = id
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

    def getId(self):
        return self.id