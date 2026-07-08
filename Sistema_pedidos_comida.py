
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
