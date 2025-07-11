# Crear un diccionario de productos
productos = {

    'producto_a': {'precio': 100, 'cantidad': 20},

    'producto_b': {'precio': 150, 'cantidad': 15},

    'producto_c': {'precio': 200, 'cantidad': 10}

}


# Acceder al precio del producto A
precio_producto_a = productos['producto_a']['precio']


# Modificar la cantidad del producto B
productos['producto_b']['cantidad'] = 12
print(productos)

# Calcular el valor total del inventario

valor_total = 0

for producto, info in productos.items():
    valor_total += info['precio'] * info['cantidad']

 
print(f"Valor total del inventario: {valor_total}")