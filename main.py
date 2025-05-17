a3 = True
while a3:
    print("1 Soma")
    print("2 Subtrair")
    print("3 Dividir")
    print("4 Multiplicar")
    print("5 Sair")

    escolha = int(input("Escolha a opção: "))
    if escolha == 1:
        escolha1 = int(input("Primeiro Numero: "))
        escolha2 = int(input("Segundo Numero: "))
        print (escolha1 + escolha2)
    elif escolha == 2:
        escolha1 = int(input("Primeiro Numero:"))
        escolha2 = int(input("Segundo Numero: "))
        print (escolha1 - escolha2)
    elif escolha == 3:
        escolha1 = int(input("Primeiro Numero:"))
        escolha2 = int(input("Segundo Numero: "))
        print (escolha / escolha2)
    elif escolha == 4:
        escolha1 = int(input("Primeiro Numero: "))
        escolha2 = int(input("Segundo Numero: "))
        print (escolha1 * escolha2)
    
    if escolha == 5:
        print("Adios")
        a3 = False