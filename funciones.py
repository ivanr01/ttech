#una funcion es un bloque de codigo, las funciones se pueden reutilizar. algunas de las funciones propias de python son print() input()max() min()

#estructura de funciones

# def nombre(param1, param2):
#   inst1
#   inst2
#return valor

#def es una palabra reservada para definir una funcion  

def suma(valor1, valor2):
    valor1+valor2
    return



def imprimir(nombre):
    print(nombre)

#llamando a la funcion con el nombre y el argumento como parametro

imprimir("John")

#reutilizando la funcion
diccionarioDinosaurios = {
    "nombre": "velociraptor",
    "velocidadKH": "100"
}

imprimir(diccionarioDinosaurios)

#calcular sueldo de empleados dependiendo de unas caracteristicas

def calculoSueldo(empleado):
    nombre = empleado["nombre"]
    tipo = empleado["tipo"]
    if tipo == "D":
        sueldo = 2000000
    elif tipo == "A":
        sueldo = 1000000
    else:
        sueldo = "NA"
    sueldoEmpleado = {
        "nombre":nombre,
        "sueldo":sueldo,
        "tipo": tipo
    }
    return sueldoEmpleado


empleado = {
    "idEmpleado": "187654",
    "nombre": "Juan Perez",
    "tipo": "D"
}

print(calculoSueldo(empleado))
