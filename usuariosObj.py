class usuariosObj:
    def __init__(
        self,
        id,
        nombre,
        apellidos,
        correo,
        usuario,
    ):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.usuario = usuario
    def getId(self):
        return self.id