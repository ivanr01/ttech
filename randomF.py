#Nos permite generar selecciones pseudo aleatorios entre valores o secuencias

#importamos todas las funcionalidades del modulo con *
from random import *
#randint tiene en cuenta dos parametros, devuelve un entero entre los dos parametros ingresados
aleatorio = randint(1,87)
print(aleatorio)

#usamos 
aleatorioR = random()
print(aleatorioR)


listaCandidatos = ["Raul", "Daniel", "Jorge"]
choiceCandidatos = choice(listaCandidatos)

print(choiceCandidatos)

shuffleCandidatos= shuffle(listaCandidatos)
print(listaCandidatos)