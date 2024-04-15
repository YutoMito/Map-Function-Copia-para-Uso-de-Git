def cuadrado(x):
  return x ** 2

numeros = [1, 2, 3, 4, 5]

# Usando map() para aplicar la función cuadrado a cada elemento de la lista numeros
resultado = list(map(cuadrado, numeros))

# Convertir el resultado a una lista para visualización
#resultado_lista = list(resultado)

print(resultado)  # Salida: [1, 4, 9, 16, 25]

######################


