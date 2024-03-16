#muestra el posicionamiento y el valor 

saludo = "hola payase"
saludoLista = list(saludo)

for letrita in enumerate(saludoLista):
    print(letrita)

for index, item in enumerate(saludoLista): 
    print(index, item)