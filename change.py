def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto: \n{expense}")
    print(f"Ingresar Dinero recibido: \n{money}")
    print(f"\nVuelto \n")
    print(f"Pesos: \n {int(money-expense)}")
    print(f"Centavos: \n{int(((money-expense)-int(money-expense))*100)}")
