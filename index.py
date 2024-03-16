saludo = "Hola, buen dia"

#count nos dice el numero de veces que se repite un caracter o un conjunto de caracteres

#podemos encontrar la ubicacion de un caracter con find rfind index y rindex

#isdigit nos permite saber si todos los caracteres son numericos

#join nos permite crear una cadena con los elementos de una lista, es uno de los metodos mas utilizados 

#verificamos longitud con len 

#listas pueden cambiar con el paso del tiempo y pueden tener elementos duplicados 

#en las listas usamos las funciones append() para agregar elementos pop() para eliminar elementos

#diccionarios tienen clave valor, son mutables, no tienen orden

#booleanos son datos verdaderos o falsos y son el resultado de operadores logicos y los condicionales

textoUsuario= input("Por favor digame lo que usted quiera: ").lower()
letrasUsuario=input("Por favor ingrese tres letras: ").lower()

letrasUsuario = list(letrasUsuario)

print(letrasUsuario)

conteo0=textoUsuario.count(letrasUsuario[0])
conteo1=textoUsuario.count(letrasUsuario[1])
conteo2=textoUsuario.count(letrasUsuario[2])

mensajeFinal = f"""
La letra {letrasUsuario[0]} aparece {conteo0} veces 
La letra {letrasUsuario[1]} aparece {conteo1} veces 
La letra {letrasUsuario[1]} aparece {conteo2} veces 
"""

print(mensajeFinal)


#contar numero de palabras
listaPalabras = textoUsuario.split(" ")
print("El texto ingresado tiene "+  str(len(listaPalabras)) + " palabras")


#mostrar primera y ultima letra
primeraLetra= textoUsuario[0]
ultimaLetra = textoUsuario[-1]

print(f"""
La primera letra es {primeraLetra}
la ultima letra es {ultimaLetra}
""")

print(listaPalabras)

#revertir lista y hacer un string
listaPalabras.reverse()

print(listaPalabras)

fraseReves= " ".join(listaPalabras)

print(fraseReves)


#saber si la palabra python esta en la frase
pythonBool = "python" in listaPalabras

if pythonBool == True :
    print("si esta la palabra python en el texto")

else: 
    print("python no esta dentro del texto") 


