class categoriaObj:
    def __init__(
        self,
        id,
        categoria,
        codigo,
    ):
        self.id = id
        self.categoria = categoria
        self.codigo = codigo

    def getId(self):
        return self.id
    
    def getcategoria(self):
        return self.categoria

    def getcodigo(self):
        return self.codigo