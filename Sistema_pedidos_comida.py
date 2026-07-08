
# BASE DE DATOS (MENU FIJO) 
menu = {
    "Entradas": {
        "Rabas": 2200.0,
        "Papas con chedar y bacon": 1900.0,
        "Picada de fiambres (para compartir)": 5800.0 
    },
    "Principales": {
        "Milanesa napolitana con papas fritas": 3900.0,
        "pizza": 5000.0,
        "hamburguesa": 3500.0
    },
    "Bebidas": {
        "Agua": 700.0,
        "Gaseosa": 900.0,
        "Cerveza": 1200.0
    },
    "Postres": {
        "Flan": 1000.0,
        "Helado": 1300.0,
        "Tiramisu": 1500.0
    }
}

# MEMORIA DEL DIA
caja_total = 0.0
contador_clientes = 0

#  FUNCIONES DEL PEDIDO 
def mostrar_categorias():
    print("\n--- CATEGORIAS ---")
    categorias = list(menu.keys())
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")
    print(f"{len(categorias)+1}. Finalizar pedido")
    return categorias

def mostrar_productos(categoria):
    print(f"\n--- {categoria.upper()} ---")
    productos = list(menu[categoria].items())
    for i, (nombre, precio) in enumerate(productos, start=1):
        print(f"{i}. {nombre} - ${precio:.2f}")
    return productos

# VALIDACIONES (CAPA DE SEGURIDAD)
def validar_entero(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < minimo or valor > maximo:
                print(f"Error: Ingrese un número entre {minimo} y {maximo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número entero valido.")

def validar_cantidad(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < 1 or valor > 50:
                print("Error: Ingrese un número entre 1 y 50")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número entero valido.")

def validar_si_no(mensaje):
    while True:
        entrada = input(mensaje).strip().upper()
        if entrada in ("SI", "NO"):
            return entrada
        print("Error: Ingrese 'SI' o 'NO'.")

# MEDIOS DE PAGO
def elegir_medio_pago():
    print("\n--- MEDIO DE PAGO ---")
    print("1. Efectivo (10% de descuento)")
    print("2. Debito (5% de descuento)")
    print("3. Credito (sin descuento)")
    print("4. Transferencia (8% de descuento)")
    opcion = validar_entero("Elija el medio de pago (1-4): ", 1, 4)
    if opcion == 1:
        return "Efectivo", 0.10
    elif opcion == 2:
        return "Debito", 0.05
    elif opcion == 3:
        return "Credito", 0.0
    else:
        return "Transferencia", 0.08

# FUNCION PARA CREAR PEDIDO
def crear_pedido():
    global caja_total, contador_clientes

    carrito = []       # Lista de elementos (nombre_producto, cantidad, subtotal_item)
    subtotal = 0.0      # Acumulador del pedido actual

    print("\n===== NUEVO PEDIDO =====")

    while True:
        categorias = mostrar_categorias()
        opcion_cat = validar_entero("Elija una categoria: ", 1, len(categorias)+1)

        # Opción de finalizar
        if opcion_cat == len(categorias) + 1:
            if len(carrito) == 0:
                print("Error: El carrito está vacío, agregue al menos un producto.")
                continue
            break

        categoria_elegida = categorias[opcion_cat - 1]
        productos = mostrar_productos(categoria_elegida)

        opcion_prod = validar_entero("Elija un producto: ", 1, len(productos))
        nombre_producto, precio_unitario = productos[opcion_prod - 1]

        cantidad = validar_cantidad(f"Cantidad de '{nombre_producto}': ")

        subtotal_item = precio_unitario * cantidad
        subtotal += subtotal_item
        carrito.append((nombre_producto, cantidad, subtotal_item))

        print(f"Agregado: {cantidad} x {nombre_producto} = ${subtotal_item:.2f}")

        seguir = validar_si_no("¿Desea agregar otro producto? (SI/NO): ")
        if seguir == "NO":
            break

    # RESUMEN DEL PEDIDO
    print("\n--- RESUMEN DEL PEDIDO ---")
    for nombre_producto, cantidad, subtotal_item in carrito:
        print(f"{cantidad} x {nombre_producto} = ${subtotal_item:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")

    # MEDIO DE PAGO Y DESCUENTO 
    medio_pago, porcentaje_descuento = elegir_medio_pago()
    descuento = subtotal * porcentaje_descuento
    total_final = subtotal - descuento

    print(f"\nMedio de pago: {medio_pago}")
    print(f"Descuento aplicado: ${descuento:.2f} ({porcentaje_descuento*100:.0f}%)")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")

    # ACTUALIZAR MEMORIA DEL DIA
    caja_total += total_final
    contador_clientes += 1

    print("\nPedido registrado con éxito!.\n")


    # VER ESTADÍSTICAS DEL DÍA
def ver_estadisticas():
    print("\n===== ESTADISTICAS DEL DIA =====")
    print(f"Clientes atendidos: {contador_clientes}")
    print(f"Caja total: ${caja_total:.2f}")
    if contador_clientes > 0:
        promedio = caja_total / contador_clientes
        print(f"Ticket promedio: ${promedio:.2f}")
    print("=================================\n")
