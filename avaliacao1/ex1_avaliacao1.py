resultado = 0
opcao = 0

while opcao != "s":
    print("""
    -------- CALCULADORA PASTRELLO --------
    ***************************************

        -------- menu de opções --------
        [+] ...................... Somar
        [-] ................... Subtrair
        [*] ................ Multiplicar
        [/] .................... Dividir
        [0] ............ Zerar resultado
        [s] ....................... Sair

    ***************************************
    """)

    print(">> Resultado atual: ", resultado)

    opcao = input("Escolha uma opção: ")

    if opcao == "+":
        num = input("Digite um número para SOMAR. Digite [v] para voltar ao menu: ")
        while num != "v":
            resultado += float(num)
            print("Resultado = ", resultado)
            num = input("Digite um novo número para SOMAR. Digite [v] para voltar ao menu: ")

    elif opcao == "-":
        num = input("Digite um número para SUBTRAIR. Digite [v] para voltar ao menu: ")
        while num != "v":
            resultado -= float(num)
            print("Resultado = ", resultado)
            num = input("Digite um novo número para SUBTRAIR. Digite [v] para voltar ao menu: ")

    elif opcao == "*":
        num = input("Digite um número para MULTIPLICAR. Digite [v] para voltar ao menu: ")
        while num != "v":
            resultado *= float(num)
            print("Resultado = ", resultado)
            num = input("Digite um novo número para MULTIPLICAR. Digite [v] para voltar ao menu: ")

    elif opcao == "/":
        num = input("Digite um número para DIVIDIR. Digite [v] para voltar ao menu: ")
        while num != "v":
            resultado /= float(num)
            print("Resultado = ", resultado)
            num = input("Digite um novo número para DIVIDIR. Digite [v] para voltar ao menu: ")

    elif opcao == "0":
        resultado = 0
        print("\n - RESULTADO ZERADO - \n")

    elif opcao == "s":
        break

    else:
        print("\n - OPÇÃO INVÁLIDA - \n")

