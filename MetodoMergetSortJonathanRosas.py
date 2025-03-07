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

Empleados_ordenados_edad = Merget_sort(Empleados, "edad")
Empleados_ordenados_salario = Merget_sort(Empleados, "salario")

valor_buscar = int(input("Ingrese la edad o el salario del empleado que desea buscar: "))

empleado = busqueda_binaria(Empleados_ordenados_edad, valor_buscar, "edad")
if not empleado:
    empleado = busqueda_binaria(Empleados_ordenados_salario, valor_buscar, "salario")

if empleado:
    print("\nEmpleado encontrado:")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Edad: {empleado['edad']}")
    print(f"Salario: {empleado['salario']}")
else:
    print("\nNo se encontró un empleado con ese criterio.")
     
print(Merget_sort(Empleados))

     
