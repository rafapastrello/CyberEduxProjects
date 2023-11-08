import adivinhacao
import forca

def escolhe_jogo():
    opcao = input("""

    ___________________________________________
    |                                         |
    |          ESCOLHA O SEU JOGO!!!          |
    |_________________________________________|


            *********************************
            ____________ JOGOS ____________

                [1] --------- Adivinhação
                [2] --------------- Forca
                _________________________
            *********************************


        >>> Escolha a opção: """)

    if opcao  == '1':
        print('\n - JOGANDO ADIVINHAÇÃO - \n')
        adivinhacao.jogar()
    elif opcao == '2':
        print('\n - JOGANDO FORCA - \n')
        forca.jogar()
    else:
        print(' - OPÇÃO INVÁLIDA!!! - ')

if __name__ == '__main__':
    escolhe_jogo()