class administradorObj:
    def __init__(
        self,
        id,
        usuario,
        contrasenna,
        correo,
        nombre,
    ):
        self.id = id
        self.usuario = usuario
        self.contrasenna = contrasenna
        self.correo = correo
        self.nombre = nombre

    def getId(self):
        return self.id