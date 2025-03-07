empleados = [
    {"nombre": "Carlos", "edad": 29, "salario": 3000},
    {"nombre": "Ana", "edad": 25, "salario": 3500},
    {"nombre": "Luis", "edad": 32, "salario": 4000},
    {"nombre": "Marta", "edad": 28, "salario": 3200},
    {"nombre": "Pedro", "edad": 35, "salario": 4200},
    {"nombre": "Elena", "edad": 27, "salario": 2800},
    {"nombre": "Sofia", "edad": 30, "salario": 3100},
    {"nombre": "Javier", "edad": 26, "salario": 3300}
]

def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][clave]
    left = [x for x in lista if x[clave] < pivote]
    medio = [x for x in lista if x[clave] == pivote]
    right = [x for x in lista if x[clave] > pivote]
    return quick_sort(left, clave) + medio + quick_sort(right, clave)

def busqueda_binaria(lista, clave, valor_buscado):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][clave] == valor_buscado:
            return lista[medio]
        elif lista[medio][clave] < valor_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

empleados_ordenados_nombre = quick_sort(empleados, "nombre")
print("\nLista ordenada por nombre:")
for emp in empleados_ordenados_nombre:
    print(emp)

empleados_ordenados_salario = quick_sort(empleados, "salario")

salario_a_buscar = 3200  # Puedes cambiar el valor aquí
resultado = busqueda_binaria(empleados_ordenados_salario, "salario", salario_a_buscar)

print("\nResultado de la búsqueda binaria por salario:")
if resultado:
    print(resultado)
else:
    print("Empleado no encontrado")
