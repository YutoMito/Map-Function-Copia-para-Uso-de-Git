def cuadrado(x):
  return x ** 2

numeros = [1, 2, 3, 4, 5]

# Usando map() para aplicar la función cuadrado a cada elemento de la lista numeros
resultado = list(map(cuadrado, numeros))

# Convertir el resultado a una lista para visualización
#resultado_lista = list(resultado)

print(resultado)  # Salida: [1, 4, 9, 16, 25]

#####################

class Empleado:
  def __init__(self, nombre, cargo, salario):
    self.nombre = nombre
    self.cargo = cargo
    self.salario = salario

def __str__(self):
  return "Nombre: {}\nCargo: {}\nSalario: {}€".format(self.nombre, self.cargo, self.salario)


lista_empleados=[
Empleado("Yuto", "Gerente", 5000),
Empleado("Dione", "Vicepresidente", 3000),
Empleado("Ana", "Vendedor", 1500),
Empleado("Pedro", "Administrativo", 1200),
Empleado("Maria", "Informatico", 2100),
]


def calculo_salario(empleado):
  if empleado.salario < 2500:
    empleado.salario *= 1.03
    return empleado

lista_salarios_comision = list(map(calculo_salario, lista_empleados))

for empleado in lista_salarios_comision:
  print(empleado)

#####################

def cuadrado(x):
  return x ** 2

numeros = [1, 2, 3, 4, 5]

# Usando map() para aplicar la función cuadrado a cada elemento de la lista numeros
resultado = list(map(cuadrado, numeros))

# Convertir el resultado a una lista para visualización
#resultado_lista = list(resultado)

print(resultado)  # Salida: [1, 4, 9, 16, 25]
