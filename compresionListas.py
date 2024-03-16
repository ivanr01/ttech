palabra =  "python"

lista=[]

for letrita in palabra: 
    lista.append(letrita)

print(lista)


#ahora con compresion de listas

listaComprimida = [letra for letra in palabra]
print(listaComprimida)