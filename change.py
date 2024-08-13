def change():
    expends = float(input("Ingresar gasto :"))
    print(f"{expends}")



    money = int(input("Dinero :"))
    print(f"{money}")

    print("\t")
    print("Vuelto")
    print("\t")

    vuelto_int = int(money - expends)
    print("Pesos :")
    print(f"{vuelto_int}")


    vuelto_float = int((((money - expends) - vuelto_int))*100)
    print("Centavos :")
    print(f"{vuelto_float}")
