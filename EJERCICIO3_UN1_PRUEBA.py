from EJERCICIOS3_UN1 import *

# LIBROS
libro1 = Libro(1, "Cien Años de Soledad", 1967, "Gabriel Garcia Marquez", "12345", "Novela")
libro2 = Libro(2, "El Hobbit", 1937, "J.R.R. Tolkien", "67890", "Fantasia")

revista1 = Revista(3, "National Geographic", 2024, 120, "Mensual")

digital1 = MaterialDigital(4, "Python Basico", 2023, "PDF", "www.biblioteca.com/python", 5.2)

print(libro1.titulo)
print(revista1.titulo)
print(digital1.titulo)

# PERSONAS
usuario1 = Usuario(1, "Carlos")
usuario2 = Usuario(2, "Ana")

bibliotecario1 = Bibliotecario(3, "Laura")

print(usuario1.nombre)
print(usuario2.nombre)
print(bibliotecario1.nombre)

# SUCURSAL
sucursal1 = Sucursal(1, "Sucursal Centro")

sucursal1.agregarMaterial(libro1)
sucursal1.agregarMaterial(libro2)
sucursal1.agregarMaterial(revista1)

print("Materiales en sucursal:", len(sucursal1.catalogoLocal))

# PRESTAMO
prestamo1 = Prestamo(
    1,
    "2025-05-01",
    "2025-05-10",
    usuario1,
    libro1
)

usuario1.solicitarPrestamo(prestamo1)

# GESTIÓN
bibliotecario1.gestionarPrestamo(prestamo1)
bibliotecario1.transferirMaterial(libro2, sucursal1)

# PENALIZACIÓN
penalizacion1 = Penalizacion(10, "Entrega tardia")

penalizacion1.calcularMulta()
penalizacion1.bloquearUsuario(usuario1)

# CATÁLOGO
catalogo = Catalogo()

catalogo.agregarMaterial(libro1)
catalogo.agregarMaterial(libro2)
catalogo.agregarMaterial(revista1)
catalogo.agregarMaterial(digital1)

resultadoAutor = catalogo.buscarPorAutor("Gabriel Garcia Marquez")

for material in resultadoAutor:
    print("Encontrado por autor:", material.titulo)

resultadoTitulo = catalogo.buscarEnTodasSucursales("El Hobbit")

for material in resultadoTitulo:
    print("Encontrado por titulo:", material.titulo)