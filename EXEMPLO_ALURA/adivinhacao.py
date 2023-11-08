import random

def jogar():
    print("""
        *******************************************
        Seja bem-vindo(a) ao jogo de adivinhação!!!
        ******************************************* """)

    contador = 0
    num_secreto = random.randrange(1,101)
    pontos = 1000

    while True:
        nivel = input("""
                ************************
                ________ NÍVEIS ________
                [1] -------------- Fácil
                [2] -------------- Médio
                [3] ------------ Difícil
                ________________________
                ************************

                Escolha a opção: """)

        if nivel == '1':
            print('>>> NÍVEL FÁCIL <<<')
            qtd_tentativas = 20
            break
        elif nivel == '2':
            print('>>> NÍVEL MÉDIO <<<')
            qtd_tentativas = 10
            break
        elif nivel == '3':
            print('>>> NÍVEL DIFÍCIL <<<')
            qtd_tentativas = 5
            break
        else:
            print('\n>>> OPÇÃO INVÁLIDA <<<')
            continue

    while True:
        print(f'\n{qtd_tentativas} tentativa(s) restante(s)\n')

        chute = int(input('>>> Informe um número entre 1 e 100: '))

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!!!')
            continue

        acertou     = chute == num_secreto
        chute_maior = chute > num_secreto
        chute_menor = chute < num_secreto

        if acertou:
            print(f'\nVocê acertou! O número secreto é {num_secreto}!!!\nVocê fez {pontos} pontos!!!')
            break
        elif chute_menor:
            print(f'\nVocê errou! O seu chute foi menor que o número secreto! Tente novamente.')
        elif chute_maior:
            print(f'\nVocê errou! O seu chute foi maior que o número secreto! Tente novamente.')
        pontos_perdidos = abs(num_secreto - chute)
        pontos -= pontos_perdidos

        qtd_tentativas -= 1

        if qtd_tentativas == contador:
            print('\nAs tentativas acabaram, fim do jogo!!!')
            print(f'Jogo finalizado com {pontos} pontos')
            break

if __name__ == '__main__':
    jogar()