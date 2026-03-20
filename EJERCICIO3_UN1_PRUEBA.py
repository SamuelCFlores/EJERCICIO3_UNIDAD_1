from EJERCICIOS3_UN1 import *

### PRUEBA CLASES
# Clase 1: Material

# 1-10 base

m1 = Material(1, "Material 1", 2000)
m2 = Material(2, "Material 2", 2001)    
m3 = Material(3, "Material 3", 2002)
m4 = Material(4, "Material 4", 2003)
m5 = Material(5, "Material 5", 2004)
m6 = Material(6, "Material 6", 2005)
m7 = Material(7, "Material 7", 2006)
m8 = Material(8, "Material 8", 2007)
m9 = Material(9, "Material 9", 2008)
m10 = Material(10, "Material 10", 2009)

Materiales = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

for m in Materiales:
    print(f"ID: {m.idMaterial} // Titulo: {m.titulo} // Año: {m.añoPublicacion} // Disponible: {m.disponible}")

# Clase 2: Libro

# 1-5 heredados
l1 = Libro(1, "Material 1", 2000, "Autor1", "111", "Gen")
l2 = Libro(2, "Material 2", 2001, "Autor2", "222", "Gen")
l3 = Libro(3, "Material 3", 2002, "Autor3", "333", "Gen")
l4 = Libro(4, "Material 4", 2003, "Autor4", "444", "Gen")
l5 = Libro(5, "Material 5", 2004, "Autor5", "555", "Gen")

# 6-10 nuevos
l6 = Libro(11, "Cien años", 1967, "Gabo", "666", "Novela")
l7 = Libro(12, "1984", 1949, "Orwell", "777", "Distopía")
l8 = Libro(13, "It", 1986, "King", "888", "Terror")
l9 = Libro(14, "Drácula", 1897, "Stoker", "999", "Terror")
l10 = Libro(15, "Odisea", -800, "Homero", "1010", "Épico")

Libros = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

for l in Libros:
    print(f"ID: {l.idMaterial} // Titulo: {l.titulo} // Autor: {l.autor} // Genero: {l.genero}")

# Clase 3: Revista

# 6-10 heredados
# usamos los ids 6 al 10 que ya existían en Material
r1 = Revista(6, "Material 6", 2005, 1, "Mensual")
r2 = Revista(7, "Material 7", 2006, 2, "Mensual")
r3 = Revista(8, "Material 8", 2007, 3, "Mensual")
r4 = Revista(9, "Material 9", 2008, 4, "Mensual")
r5 = Revista(10, "Material 10", 2009, 5, "Mensual")

# 11-15 nuevos
# estos ya son revistas nuevas con ids diferentes para no repetir
r6 = Revista(11, "NatGeo", 2023, 6, "Mensual")
r7 = Revista(12, "Time", 2023, 7, "Semanal")
r8 = Revista(13, "Forbes", 2023, 8, "Mensual")
r9 = Revista(14, "Science", 2023, 9, "Semanal")
r10 = Revista(15, "Nature", 2023, 10, "Semanal")

Revistas = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]

for r in Revistas:
    print(f"ID: {r.idMaterial} // Titulo: {r.titulo} // Edicion: {r.edicion} // Periodicidad: {r.periodicidad}")


# Clase 4: MaterialDigital

# 6-10 heredados
# usamos materiales del 6 al 10 como digitales
md1 = MaterialDigital(6, "Material 6", 2005, "PDF", "url1", 5)
md2 = MaterialDigital(7, "Material 7", 2006, "PDF", "url2", 6)
md3 = MaterialDigital(8, "Material 8", 2007, "PDF", "url3", 7)
md4 = MaterialDigital(9, "Material 9", 2008, "PDF", "url4", 8)
md5 = MaterialDigital(10, "Material 10", 2009, "PDF", "url5", 9)

# 11-15 nuevos
# nuevos materiales digitales
md6 = MaterialDigital(11, "Curso Python", 2022, "MP4", "url6", 1000)
md7 = MaterialDigital(12, "Curso Java", 2021, "MP4", "url7", 900)
md8 = MaterialDigital(13, "HTML", 2020, "PDF", "url8", 3)
md9 = MaterialDigital(14, "CSS", 2021, "MP4", "url9", 800)
md10 = MaterialDigital(15, "Linux", 2019, "PDF", "url10", 7)

MaterialesDigitales = [md1, md2, md3, md4, md5, md6, md7, md8, md9, md10]

for md in MaterialesDigitales:
    print(f"ID: {md.idMaterial} // Titulo: {md.titulo} // Tipo: {md.tipoArchivo} // Tamaño: {md.tamañoMB}")

# Clase 5: Persona

# 1-10 base
p1 = Persona(1, "Samuel")
p2 = Persona(2, "Ana")
p3 = Persona(3, "Luis")
p4 = Persona(4, "Carlos")
p5 = Persona(5, "Sofía")
p6 = Persona(6, "María")
p7 = Persona(7, "Pedro")
p8 = Persona(8, "Lucía")
p9 = Persona(9, "Jorge")
p10 = Persona(10, "Elena")

Personas = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

for p in Personas:
    print(f"ID: {p.idPersona} // Nombre: {p.nombre}")

# Clase 6: Usuario

# 1-5 heredados
# usamos personas como usuarios
u1 = Usuario(1, "Samuel")
u2 = Usuario(2, "Ana")
u3 = Usuario(3, "Luis")
u4 = Usuario(4, "Carlos")
u5 = Usuario(5, "Sofía")

# 6-10 nuevos
# nuevos usuarios con ids diferentes
u6 = Usuario(11, "María")
u7 = Usuario(12, "Pedro")
u8 = Usuario(13, "Lucía")
u9 = Usuario(14, "Jorge")
u10 = Usuario(15, "Elena")


Usuarios = [u1,u2,u3,u4,u5,u6,u7,u8,u9,u10]

for u in Usuarios:
    print(f"ID: {u.idPersona} // Nombre: {u.nombre} // Limite: {u.limitePrestamos}")

# Clase 7: Bibliotecario

# 6-10 heredados
# usamos personas del 6 al 10 como bibliotecarios
b1 = Bibliotecario(6, "María")
b2 = Bibliotecario(7, "Pedro")
b3 = Bibliotecario(8, "Lucía")
b4 = Bibliotecario(9, "Jorge")
b5 = Bibliotecario(10, "Elena")

# 11-15 nuevos
# nuevos bibliotecarios
b6 = Bibliotecario(16, "Admin1")
b7 = Bibliotecario(17, "Admin2")
b8 = Bibliotecario(18, "Admin3")
b9 = Bibliotecario(19, "Admin4")
b10 = Bibliotecario(20, "Admin5")


Bibliotecarios = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]

for b in Bibliotecarios:
    print(f"ID: {b.idPersona} // Nombre: {b.nombre}")

# Clase 8 : Sucursal

s1 = Sucursal(1, "Centro")
s2 = Sucursal(2, "Norte")
s3 = Sucursal(3, "Sur")
s4 = Sucursal(4, "Este")
s5 = Sucursal(5, "Oeste")
s6 = Sucursal(6, "BUAP")
s7 = Sucursal(7, "UNAM")
s8 = Sucursal(8, "IPN")
s9 = Sucursal(9, "Tec")
s10 = Sucursal(10, "Digital")

Sucursales = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

for s in Sucursales:
    print(f"ID: {s.idSucursal} // Nombre: {s.nombre}")

# Clase 9 : Prestamo
pr1 = Prestamo(1, "2026-03-01", "2026-03-10", u1, l1)
pr2 = Prestamo(2, "2026-03-02", "2026-03-11", u2, l2)
pr3 = Prestamo(3, "2026-03-03", "2026-03-12", u3, l3)
pr4 = Prestamo(4, "2026-03-04", "2026-03-13", u4, r1)
pr5 = Prestamo(5, "2026-03-05", "2026-03-14", u5, r2)

pr6 = Prestamo(6, "2026-03-06", "2026-03-15", u6, md6)
pr7 = Prestamo(7, "2026-03-07", "2026-03-16", u7, md7)
pr8 = Prestamo(8, "2026-03-08", "2026-03-17", u8, l6)
pr9 = Prestamo(9, "2026-03-09", "2026-03-18", u9, r6)
pr10 = Prestamo(10, "2026-03-10", "2026-03-19", u10, md8)

Prestamos = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9,pr10]

for pr in Prestamos:
    print(f"ID: {pr.idPrestamo} // Usuario: {pr.usuario.nombre} // Material: {pr.material.titulo}")

# Clase 10 : Penalizacion

pen1 = Penalizacion(50, "Retraso")
pen2 = Penalizacion(30, "Daño")
pen3 = Penalizacion(20, "Leve")
pen4 = Penalizacion(100, "Pérdida")
pen5 = Penalizacion(60, "Retraso")
pen6 = Penalizacion(40, "Daño")
pen7 = Penalizacion(25, "Leve")
pen8 = Penalizacion(80, "Pérdida")
pen9 = Penalizacion(35, "Retraso")
pen10 = Penalizacion(45, "Daño")

Penalizaciones = [pen1,pen2,pen3,pen4,pen5,pen6,pen7,pen8,pen9,pen10]

for p in Penalizaciones:
    print(f"Monto: {p.monto} // Motivo: {p.motivo} // Pagada: {p.pagada}")

# Clase 11: Catalogo

# 1-10 base
c1 = Catalogo()
c2 = Catalogo()
c3 = Catalogo()
c4 = Catalogo()
c5 = Catalogo()
c6 = Catalogo()
c7 = Catalogo()
c8 = Catalogo()
c9 = Catalogo()
c10 = Catalogo()

Catalogos = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

# agrego algunos materiales de ejemplo
c1.agregarMaterial(l1)
c1.agregarMaterial(r1)
c2.agregarMaterial(l2)
c3.agregarMaterial(md1)

for i, c in enumerate(Catalogos, start=1):
    print(f"Catalogo {i} // Materiales: {len(c.materiales)}")

### PRUEBA METODOS
# Clase 1 : Material - Metodos
# no tiene metodos

print("Material no tiene metodos")

# Clase 2 : Libro - Metodos
# no tiene metodos propios (hereda de Material)

print("Libro no tiene metodos")

# Clase 3 : Revista - Metodos
# no tiene metodos

print("Revista no tiene metodos")

# Clase 4 : MaterialDigital - Metodos
# no tiene metodos

print("MaterialDigital no tiene metodos")

# Clase 5 : Persona - Metodos
# no tiene metodos

print("Persona no tiene metodos")

# Clase 6 : Usuario - Metodos

print("PRUEBA solicitarPrestamo")

u1.solicitarPrestamo(pr1)
u1.solicitarPrestamo(pr2)
u1.solicitarPrestamo(pr3)

# este ya no debería dejar
u1.solicitarPrestamo(pr4)

print(f"Prestamos activos: {len(u1.listaActiva)}")

# Clase 7 : Bibliotecario - Metodos

print("PRUEBA gestionarPrestamo")
b1.gestionarPrestamo(pr1)

print("\nPRUEBA transferirMaterial")

print(f"Antes: {len(s1.catalogoLocal)}")
b1.transferirMaterial(l1, s1)
print(f"Despues: {len(s1.catalogoLocal)}")

# Clase 8 : Sucursal - Metodos

print("PRUEBA agregarMaterial")

print(f"Antes: {len(s1.catalogoLocal)}")
s1.agregarMaterial(l2)
print(f"Despues: {len(s1.catalogoLocal)}")

# Clase 9 : Prestamo - Metodos
# no tiene metodos

print("Prestamo no tiene metodos")

# Clase 10 : Penalizacion - Metodos

print("PRUEBA calcularMulta")
pen1.calcularMulta()

print("\nPRUEBA bloquearUsuario")
pen1.bloquearUsuario(u1)

# Clase 11 : Catalogo - Metodos
# usamos un catalogo con datos
catalogo = c1

print("PRUEBA buscarPorAutor")

res1 = catalogo.buscarPorAutor("Autor1")

for m in res1:
    print(f"Titulo: {m.titulo} // Autor: {m.autor}")

print("\nPRUEBA buscarPorTitulo")

res2 = catalogo.buscarEnTodasSucursales("Material 1")

for m in res2:
    print(f"ID: {m.idMaterial} // Titulo: {m.titulo}")

# PRUEBA COMPLETA DEL SISTEMA (LOGICA)

print(" --- INICIO PRUEBA GENERAL ---")

# -------------------------------
# 1. SUCURSALES
# -------------------------------
s1 = Sucursal(1, "Centro")
s2 = Sucursal(2, "Norte")

# -------------------------------
# 2. MATERIALES
# -------------------------------
l1 = Libro(1, "1984", 1949, "Orwell", "111", "Distopia")
r1 = Revista(2, "NatGeo", 2023, 1, "Mensual")
md1 = MaterialDigital(3, "Curso Python", 2022, "MP4", "url", 500)

# agregar a sucursal
s1.agregarMaterial(l1)
s1.agregarMaterial(r1)

print(f"Sucursal {s1.nombre} tiene {len(s1.catalogoLocal)} materiales")

# -------------------------------
# 3. USUARIO Y BIBLIOTECARIO
# -------------------------------
u1 = Usuario(1, "Samuel")
b1 = Bibliotecario(2, "Admin")

# -------------------------------
# 4. PRÉSTAMO
# -------------------------------
pr1 = Prestamo(1, "2026-03-01", "2026-03-10", u1, l1)

# usuario solicita préstamo
print()
print("--- Usuario solicita préstamo ---")
u1.solicitarPrestamo(pr1)

# bibliotecario gestiona
print()
print("--- Bibliotecario gestiona ---")
b1.gestionarPrestamo(pr1)

# -------------------------------
# 5. TRANSFERIR MATERIAL
# -------------------------------
print()
print("--- Transferencia de material ---")

print(f"Antes en {s2.nombre}: {len(s2.catalogoLocal)}")
b1.transferirMaterial(r1, s2)
print(f"Después en {s2.nombre}: {len(s2.catalogoLocal)}")

# -------------------------------
# 6. PENALIZACIÓN
# -------------------------------
print()
print("--- Penalización ---")

pen1 = Penalizacion(50, "Retraso")
pen1.calcularMulta()
pen1.bloquearUsuario(u1)

# -------------------------------
# 7. CATÁLOGO
# -------------------------------
print()
print("--- Catálogo ---")

catalogo = Catalogo()
catalogo.agregarMaterial(l1)
catalogo.agregarMaterial(r1)
catalogo.agregarMaterial(md1)

# buscar por autor
print()
print("Buscar por autor (Orwell):")
res1 = catalogo.buscarPorAutor("Orwell")
for m in res1:
    print(f"{m.titulo} // {m.autor}")

# buscar por título
print()
print("Buscar por titulo (1984):")
res2 = catalogo.buscarEnTodasSucursales("1984")
for m in res2:
    print(f"{m.idMaterial} // {m.titulo}")

# -------------------------------
# FIN
# -------------------------------
print()
print("--- FIN DE PRUEBA ---")
