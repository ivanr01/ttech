#el codigo se evalua en diferentes casos que pueden ser condicionales 

serie = "N-02"

if serie == "N-01":
    print("Nokia")
elif serie == "N-02":
    print("Samsung")
elif serie == "N-03":
    print("Motorola")
else:
    print("Modelo no encontrado")


#ahora utilizaremos match
#el else se utiliza en match con "case_"
match serie: 
    case "N-01":
        print("Nokia")
    case "N-02":
        print("Samsung")
    case "N-03":
        print("Motorola")
    case _: 
        print("Modelo no encontrado")
