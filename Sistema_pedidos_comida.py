
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
