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
    
    vuelto_completo = money - expends
    pesos = int(vuelto_completo)  
    centavos = int(round((vuelto_completo - pesos) * 100))  # Parte decimal (centavos)
    
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")

change()
