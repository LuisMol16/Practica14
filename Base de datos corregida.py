contraseña = ""
while contraseña != "yuki":
    contraseña = input("Introduce la contraseña: ")
print("Contraseña correcta!")

inventario = { 
    "Camiseta Básica": {
        "precio": 200, 
        "características": [
            "Corte holgado", 
            "Color verde", 
            "Tela de algodón", 
            "Cuello redondo", 
            "Manga corta", 
            "No se arruga", 
            "Lavar a máquina", 
            "Unisex", 
            "Talla estándar", 
            "Secado rápido"
        ]
    },
    "Jeans Ajustados": {
        "precio": 600, 
        "características": [
            "Mezclilla clara", 
            "Corte ajustado", 
            "Cintura alta", 
            "5 bolsillos", 
            "Elástico", 
            "Cremallera metálica", 
            "Lavado vintage", 
            "Durabilidad alta", 
            "Unisex", 
            "Resistente a decoloración"
        ]
    },
    "Chaqueta de Cuero": {
        "precio": 1200, 
        "características": [
            "Cuero sintético", 
            "Color negro", 
            "Cierre frontal", 
            "Bolsillos exteriores", 
            "Corte entallado", 
            "Forro de poliéster", 
            "Cuello elevado", 
            "Ideal para invierno", 
            "Resistente al agua", 
            "Durabilidad alta"
        ]
    },
    "Sudadera con Capucha": {
        "precio": 450, 
        "características": [
            "Estampado de Pokémon", 
            "Con capucha ajustable", 
            "Bolsillo delantero", 
            "Corte relajado", 
            "Tela afelpada", 
            "Color gris", 
            "Unisex", 
            "Tallas amplias", 
            "Lavar a máquina", 
            "No pierde color"
        ]
    },
    "Zapatos Deportivos": {
        "precio": 1500, 
        "características": [
            "Marca Adidas", 
            "Diseño ergonómico", 
            "Color blanco", 
            "Cordones ajustables", 
            "Suela antideslizante", 
            "Amortiguación EVA", 
            "Ligereza extrema", 
            "Transpirables", 
            "Resistentes al agua", 
            "Para correr"
        ]
    },
    "Pantalones Cortos": {
        "precio": 300, 
        "características": [
            "Mezclilla oscura", 
            "Corte regular", 
            "Cintura ajustable", 
            "Bolsillos profundos", 
            "Costuras reforzadas", 
            "No se arruga", 
            "Tela elástica", 
            "Unisex", 
            "Secado rápido", 
            "Durabilidad alta"
        ]
    },
    "Blusa de Seda": {
        "precio": 800, 
        "características": [
            "Color amarillo", 
            "Diseño floral", 
            "Tela de seda", 
            "Manga corta", 
            "Corte holgado", 
            "Cuello en V", 
            "Ligera", 
            "Fresca", 
            "No se arruga", 
            "Lavar a mano"
        ]
    },
    "Vestido de Verano": {
        "precio": 900, 
        "características": [
            "Vestido rojo", 
            "Broche frontal", 
            "Tirantes ajustables", 
            "Tela fresca", 
            "Diseño floral", 
            "Corte acampanado", 
            "Ligero", 
            "Lavar a mano", 
            "Secado rápido", 
            "Talla estándar"
        ]
    },
    "Botines de Cuero": {
        "precio": 1700, 
        "características": [
            "Plataforma alta", 
            "Color negro", 
            "Cuero sintético", 
            "Cierre lateral", 
            "Tacón grueso", 
            "Forro interior suave", 
            "Resistentes al agua", 
            "Antideslizantes", 
            "Unisex", 
            "Durabilidad alta"
        ]
    },
    "Sombrero de Playa": {
        "precio": 250, 
        "características": [
            "Sombrero de paja", 
            "Color natural", 
            "Ala ancha", 
            "Decoración de cinta", 
            "Ligero", 
            "Protección solar", 
            "Talla única", 
            "Resistente al agua", 
            "Fácil de transportar", 
            "Diseño elegante"
        ]
    }
}

def agregar_producto(nombre, precio, caracteristicas):
    inventario[nombre] = {"precio": precio, "características": caracteristicas}
    print(f"Producto '{nombre}' agregado al inventario.")

def mostrar_inventario():
    if inventario:
        print("\nInventario actual:")
        for nombre, detalles in inventario.items():
            precio = detalles["precio"]
            caracteristicas = ", ".join(detalles["características"])
            print(f"- Producto: {nombre}, Precio: ${precio:.2f} MXM\n  Características: {caracteristicas}")
    else:
        print("El inventario está vacío.")

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"No se encontró el producto '{nombre}'.")

def modificar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre]["precio"] = nuevo_precio
        print(f"El precio del producto '{nombre}' ha sido actualizado a ${nuevo_precio:.2f} MXM.")
    else:
        print(f"No se encontró el producto '{nombre}'.")

print("╔══════════════════════════════════╗")
print("║          Bienvenido a Yuki       ║")
print("║  ¡Tu tienda de ropa favorita!    ║")
print("╚══════════════════════════════════╝")
print("\nTrabajo elaborado por: Muñoz Molina Luis Angel y Morales Carpinteyro Brayan Mauricio.")

while True:
    print("\nTienda de Ropa - Menú de Inventario")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Eliminar Producto")
    print("4. Modificar Precio")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    if opcion == "1":
        nombre = input("Nombre del Producto: ")
        precio = float(input("Precio del Producto (MXM): $"))
        caracteristicas = input("Características del Producto (separadas por comas): ").split(", ")
        agregar_producto(nombre, precio, caracteristicas)
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        nombre = input("Nombre del producto a eliminar: ")
        eliminar_producto(nombre)
    elif opcion == "4":
        nombre = input("Nombre del producto a modificar: ")
        nuevo_precio = float(input("Nuevo precio (MXM): $"))
        modificar_precio(nombre, nuevo_precio)
    elif opcion == "5":
        print("Gracias por visitar Yuki. ¡Te esperamos pronto!")
        break
    else:
        print("Opción inválida. Por favor elige una opción entre 1 y 5.")
