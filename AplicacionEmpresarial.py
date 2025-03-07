Empleados = [
    {"nombre": "Carlos", "edad": 29, "salario": 3000},
    {"nombre": "Ana", "edad": 25, "salario": 3500},
    {"nombre": "Luis", "edad": 32, "salario": 4000},
    {"nombre": "Marta", "edad": 28, "salario": 3200},
    {"nombre": "Pedro", "edad": 35, "salario": 4200},
    {"nombre": "Elena", "edad": 27, "salario": 2800},
    {"nombre": "Sofía", "edad": 30, "salario": 3100},
    {"nombre": "Javier", "edad": 26, "salario": 3300},
]

def Merget_sort(Empleados, clave):
    N = len(Empleados)
    if N <= 1:
        return Empleados

    mid  = N // 2
    left = Merget_sort(Empleados[:mid], clave)
    right = Merget_sort(Empleados[mid:], clave)

    resultado = []
    i = 0
    j = 0 

    while i < len(left) and j < len(right):
        if left[i][clave] <= right[j][clave]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

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

def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][clave]
    left = [x for x in lista if x[clave] < pivote]
    medio = [x for x in lista if x[clave] == pivote]
    right = [x for x in lista if x[clave] > pivote]
    return quick_sort(left, clave) + medio + quick_sort(right, clave)


def busqueda_binaria(Empleados, valor, clave):
    inicio, fin = 0, len(Empleados) - 1

    while inicio <= fin:
        mid = (inicio + fin) // 2
        if Empleados[mid][clave] == valor:
            return Empleados[mid] 
        elif Empleados[mid][clave] < valor:
            inicio = mid + 1
        else:
            fin = mid - 1

    return None  

while True:
    print("\nHola, bienvenido a mi aplicación Empresarial")
    print("¿Qué quieres hacer?:")
    print("1. Ordenar por edad")
    print("2. Ordenar por nombre")
    print("3. Ordenar por salario")
    print("4. Buscar por edad")
    print("5. Buscar por salario")
    print("6. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        empleados_ordenados = heap_sort(Empleados.copy(), "edad")
        print("\nEmpleados ordenados por edad:")
        for e in empleados_ordenados:
            print(e)
        break

    elif opcion == "2":
        empleados_ordenados_nombre = quick_sort(Empleados, "nombre")
        print("\nLista ordenada por nombre:")
        for e in empleados_ordenados_nombre:
            print(e)
        break    
    elif opcion == "3":
        empleados_ordenados = heap_sort(Empleados.copy(), "salario")
        print("\nEmpleados ordenados por salario:")
        for e in empleados_ordenados:
            print(e)
        break
    elif opcion == "4":
        valor = int(input("Ingrese la edad a buscar: "))
        empleados_ordenados = Merget_sort(Empleados, "edad")
        empleado = busqueda_binaria(empleados_ordenados, valor, "edad")
        if empleado:
            print(f"\nEmpleado encontrado: {empleado}")
        else:
            print("\nNo se encontró un empleado con esa edad.")
        break
    elif opcion == "5":
        valor = int(input("Ingrese el salario a buscar: "))
        empleados_ordenados = Merget_sort(Empleados, "salario")
        empleado = busqueda_binaria(empleados_ordenados, valor, "salario")
        if empleado:
            print(f"\nEmpleado encontrado: {empleado}")
        else:
            print("\nNo se encontró un empleado con ese salario.")
        break
    elif opcion == "6":
        print("Saliendo de la aplicación...")
        break
    else:
        print("\nOpción no válida. Intente de nuevo.")

     
