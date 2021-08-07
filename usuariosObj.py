class usuariosObj:
    def __init__(
        self,
        id,
        nombre,
        apellidos,
        correo,
    ):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
    def getId(self):
        return self.id