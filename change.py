def change():
    print("Ingresar gasto:")
    expends = 23.75
    print(f"{expends}")
    print("Dinero recibido")
    money = 100
    print(f"{money}")
    print("")
    print("Vuelto")
    print("")
    vuelto_int = int(money - expends)
    print("Pesos:")
    print(f"{vuelto_int}")
    vuelto_float = int((((money - expends) - vuelto_int))*100)
    print("Centavos:")
    print(f"{vuelto_float}")
