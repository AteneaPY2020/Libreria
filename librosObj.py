class librosObj:
    def __init__(
        self,
        id,
        titulo,
        autor,
        edicion,
        editorial,
        sinopsis,
        portada,
        portada_nombre,
        correlativo,
        pais,
        anno,
        ejemplares,
        disponibles,
        id_categoria,
    ):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.editorial = editorial
        self.sinopsis = sinopsis
        self.portada = portada
        self.portada_nombre = portada_nombre
        self.correlativo = correlativo
        self.pais = pais
        self.anno = anno
        self.ejemplares = ejemplares
        self.disponibles = disponibles
        self.id_categoria = id_categoria

    def getId(self):
        return self.id