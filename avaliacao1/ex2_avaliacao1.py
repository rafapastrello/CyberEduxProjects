total = 0.00

while True:
    print("""
    -------- REGISTRADORA PASTRELLO -------
    ***************************************
    
        -------- menu de opções --------
        Código                     Preço
        [1] ....................... 0,50
        [2] ....................... 1,00
        [3] ....................... 4,00
        [5] ....................... 7,00
        [9] ....................... 8,00
        [s] ........... Finalizar compra
    
    ***************************************
    """)

    item = input("Informe o item desejado: ")

    if item == "s":
        print("\n----> Total da compra: R$", total)
        break

    else:
        menu = int(item)

    if menu == 1 or menu == 2 or menu == 3 or menu == 5 or menu == 9:
        qtd = int(input("Informe a quantidade: "))

        if menu == 1:
            total = total + (0.50 * qtd)
        elif menu == 2:
            total = total + (1 * qtd)
        elif menu == 3:
            total = total + (4 * qtd)
        elif menu == 5:
            total = total + (7 * qtd)
        elif menu == 9:
            total = total + (8 * qtd)

    else:
        print("\n\n - CÓDIGO INVÁLIDO - \n")




