# EJERCICIO 3: BIBLIOTECA DIGITAL
# MATERIAL (CLASE BASE) , REPRESENTACIÓN GENÉRICA DE UN RECURSO

# 1. MODULO: DE MATERIALES (HERENENCIA)
# ATRIBUTOS: idMaterial: int, titulo: String, añoPublicacion: int, disponible: boolean

class Material:

    def __init__(self, idMaterial, titulo, añoPublicacion):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = True

# LIBRO (HEREDA DE MATERIAL) , RECURSO FÍSICO TRADICIONAL
# ATRIBUTOS: autor: String, isbn: String, genero: String

class Libro(Material):

    def __init__(self, idMaterial, titulo, añoPublicacion, autor, isbn, genero):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

# REVISTA (HEREDA DE MATERIAL) , PUBLICACIONES PERIÓDICAS
# ATRIBUTOS: edicion: int, periodicidad: String

class Revista(Material):

    def __init__(self, idMaterial, titulo, añoPublicacion, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.edicion = edicion
        self.periodicidad = periodicidad

# REVISTA (HEREDA DE MATERIAL) , PUBLICACIONES PERIÓDICAS
# ATRIBUTOS: edicion: int, periodicidad: String

class Revista(Material):

    def __init__(self, idMaterial, titulo, añoPublicacion, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.edicion = edicion
        self.periodicidad = periodicidad

# MATERIALDIGITAL (HEREDA DE MATERIAL) , RECURSOS DESCARGABLES
# ATRIBUTOS: tipoArchivo: String, urlDescarga: String, tamañoMB: float

class MaterialDigital(Material):

    def __init__(self, idMaterial, titulo, añoPublicacion, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB

# 2. MDOULO DE USUARIOS Y SEDES
# PERSONA (CLASE BASE) , IDENTIDAD BÁSICA EN EL SISTEMA
# ATRIBUTOS: idPersona: int, nombre: String

class Persona:

    def __init__(self, idPersona, nombre):
        self.idPersona = idPersona
        self.nombre = nombre

# USUARIO (HEREDA DE PERSONA) , PERSONA QUE SOLICITA PRÉSTAMOS
# ATRIBUTOS: limitePrestamos: int, listaActiva: List<Prestamo>

class Usuario(Persona):

    def __init__(self, idPersona, nombre):
        super().__init__(idPersona, nombre)
        self.limitePrestamos = 3
        self.listaActiva = []

    def solicitarPrestamo(self, prestamo):

        if len(self.listaActiva) < self.limitePrestamos:
            self.listaActiva.append(prestamo)
            print(self.nombre, "ha solicitado un préstamo")
        else:
            print("Límite de préstamos alcanzado")

# BIBLIOTECARIO (HEREDA DE PERSONA) , ADMINISTRADOR DEL CATÁLOGO Y PRÉSTAMOS
# MÉTODOS: gestionarPrestamo(), transferirMaterial()

class Bibliotecario(Persona):

    def gestionarPrestamo(self, prestamo):
        print("Préstamo gestionado")

    def transferirMaterial(self, material, sucursalDestino):
        sucursalDestino.catalogoLocal.append(material)
        print("Material transferido a", sucursalDestino.nombre)

# SUCURSAL , UBICACIÓN FÍSICA DE LOS MATERIALES
# ATRIBUTOS: idSucursal: int, nombre: String, catalogoLocal: List<Material>

class Sucursal:

    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

    def agregarMaterial(self, material):
        self.catalogoLocal.append(material)

# 3. GESTIÓN DE PRÉSTAMOS Y PENALIZACIONES
# PRESTAMO , REGISTRO DEL USO TEMPORAL DE UN MATERIAL
# ATRIBUTOS: idPrestamo: int, fechaInicio: Date, fechaDevolucion: Date, usuario: Usuario, material: Material

class Prestamo:

    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

# PENALIZACION , CONTROL DE MULTAS POR RETRASOS
# ATRIBUTOS: monto: float, motivo: String, pagada: boolean
# MÉTODOS: calcularMulta(), bloquearUsuario()

class Penalizacion:

    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo
        self.pagada = False

    def calcularMulta(self):
        print("La multa es de:", self.monto)

    def bloquearUsuario(self, usuario):
        print("Usuario bloqueado:", usuario.nombre)

# CATALOGO , HERRAMIENTA DE BÚSQUEDA GLOBAL
# MÉTODOS: buscarPorAutor(), buscarEnTodasSucursales()

class Catalogo:

    def __init__(self):
        self.materiales = []

    def agregarMaterial(self, material):
        self.materiales.append(material)

    def buscarPorAutor(self, autor):

        resultados = []

        for material in self.materiales:
            if isinstance(material, Libro) and material.autor == autor:
                resultados.append(material)

        return resultados


    def buscarEnTodasSucursales(self, titulo):

        resultados = []

        for material in self.materiales:
            if material.titulo == titulo:
                resultados.append(material)

        return resultados
