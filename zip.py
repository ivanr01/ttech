#la funcion zip() nos permite crear un iterador formado por los elementos agrupados del mismo indice 

letras = ["w", "Y"]
numeros = [4,7]

for letra, num in zip(letras, numeros):
    print(f"letra: {letra}, numero: {num}")


estudiante = ["Raul", "Ernesto"]
calificacion = [4.5,2.9]

for letra, num in zip(estudiante, calificacion):
    print(f"Estudiante: {letra}, calificacion: {num}")

