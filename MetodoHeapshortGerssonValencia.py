empleados = [
    {"nombre": "Carlos", "edad": 29, "salario": 3000},
    {"nombre": "Ana", "edad": 25, "salario": 3500},
    {"nombre": "Luis", "edad": 32, "salario": 4000},
    {"nombre": "Marta", "edad": 28, "salario": 3200},
    {"nombre": "Pedro", "edad": 35, "salario": 4200},
    {"nombre": "Elena", "edad": 27, "salario": 2800},
    {"nombre": "Sofía", "edad": 30, "salario": 3100},
    {"nombre": "Javier", "edad": 26, "salario": 3300},
]

# Ordenar por edad usando Heap Sort

def intercambiar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapify(arr, n, i, clave):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    if izquierda < n and arr[izquierda][clave] > arr[mayor][clave]:
        mayor = izquierda
    if derecha < n and arr[derecha][clave] > arr[mayor][clave]:
        mayor = derecha
    if mayor != i:
        intercambiar(arr, i, mayor)
        heapify(arr, n, mayor, clave)

def heap_sort(arr, clave):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, clave)
    for i in range(n - 1, 0, -1):
        intercambiar(arr, 0, i)
        heapify(arr, i, 0, clave)
    return arr

def Binary_search(lista, clave, valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][clave] == valor:
            return lista[medio]
        elif lista[medio][clave] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

empleados_ordenados = heap_sort(empleados.copy(), "edad")
print("Empleados ordenados por edad:")
for e in empleados_ordenados:
    print(e)
