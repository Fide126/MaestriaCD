# Crear un conjunto de clientes
clientes = {'Juan', 'María', 'Pedro', 'Ana', 'Juan'}

  

# Agregar un nuevo cliente
clientes.add('Luis')

  

# Intentar agregar un cliente duplicado
clientes.add('María')  # No tendrá efecto

  

print(clientes)  # Salida: {'Juan', 'María', 'Pedro', 'Ana', 'Luis'}
# Conjuntos de clientes que compraron en diferentes categorías
compradores_categoria_a = {'Juan', 'María', 'Ana'}
compradores_categoria_b = {'María', 'Pedro', 'Luis'}


# Obtener los clientes que compraron en ambas categorías
clientes_comunes = compradores_categoria_a.intersection(compradores_categoria_b)

print(clientes_comunes)  # Salida: {'María'}