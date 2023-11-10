# veiculos

import json
import os


def cadastrar_veiculos():
    # função para salvar veiculo

    def salvarVeiculo(veiculos):
        with open("veiculos.txt", 'w') as c:
            json.dump(veiculos, c)

            # função para carregar  o diionário "clientes"

    def carregarVeiculo():
        if not os.path.exists('veiculos.txt'):
            salvarVeiculo({})
        with open('veiculos.txt', 'r') as r:
            veiculo = json.loads(r.read())
            return veiculo

    #  função para cadastrar veículos com salvamento automatico

    def cadastrarVeiculos(veiculos):
        while True:
            fabricante = input("Digite a fabricante do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            cor = input("digite a cor do veículo: ")
            valor = input("Digite o o valor da diária do veículo: ")

            if veiculos == dict():
                codigo = 1
            else:
                codigo = max(int(key) for key in veiculos.keys()) + 1

            veiculos[codigo] = fabricante, modelo, ano, cor, valor

            continuar = input(" Dejesa cadastrar outro veículo(s/n):")

            while continuar != 's' and continuar != 'n':
                continuar = input("Coloque uma resposta válida:")

            if continuar == 'n':
                break

    # visualizar veículo

    def visualizarVeiculo(veiculos):
        print('')
        print(
            f'{"código":<6} | {"Fabricante":<15} | {"Modelo":<17} | {"Ano":<13} | {"Cor":<15} | {"Valor":<17} |')
        print("-" * 100)
        for i in veiculos.keys():
            print(
                f'{i:<6} | {veiculos[i][0]:<15} | {veiculos[i][1]:<17} | {veiculos[i][2]:<13} | {veiculos[i][3]:<15} | {veiculos[i][4]:<18}| ')
        print('')

    # Função para buscar um unico veículo

    def buscarVeiculo(veiculos):
        codigo = input("Digite o código do veículo: ")
        print('')
        print("Fabricante: ", veiculos[codigo][0])
        print("Modelo: ", veiculos[codigo][1])
        print("Ano: ", veiculos[codigo][2])
        print("Cor: ", veiculos[codigo][3])
        print("Valor da Diária:", veiculos[codigo][4])
        print('')

    # função para editar veículo

    def EditarVeiculo(veiculo):
        escolhaCodigo = input('Digite o código do Veículo :')
        print('1 - Fabricante \n 2 - Modelo \n 3 - Ano \n 4 - Cor\n 5 - Valor da Diária')

        parte = int(input('qual dado do veículo:'))
        novoAtributo = input("Dejesa substituir esse atributo pelo o que:")
        if escolhaCodigo in veiculo:
            print(veiculo[escolhaCodigo][parte - 1])
            veiculo[escolhaCodigo][parte - 1] = novoAtributo
            print("O dado do veículo foi alterado !!")
        else:
            print("Esse codigo não existe")

    # função para deletar

    def deletarVeiculo(veiculo):
        escolha = input("Insira o codigo que queira deletar:")
        deletar = veiculo.pop(escolha)
        print("Veículo deletado!")
        return deletar

    # função para mostrar o menu

    def menuVeiculo():
        print("1 - Cadastrar Veículo")
        print("2 - Visualisar Veículo")
        print("3 - Editar Veículo")
        print("4 - Deletar Veículo")
        print("5 - Buscar Veículo")
        print("6 - Voltar")

    # -------------------------------------

    while True:
        veiculos = carregarVeiculo()
        menuVeiculo()
        opcao = int(input('Escolha uma opção:'))

        if (opcao == 1):
            cadastrarVeiculos(veiculos)
            salvarVeiculo(veiculos)

        elif opcao == 2:
            visualizarVeiculo(veiculos)

        elif opcao == 3:
            EditarVeiculo(veiculos)
            salvarVeiculo(veiculos)
        elif opcao == 4:
            deletarVeiculo(veiculos)
            salvarVeiculo(veiculos)
        elif opcao == 5:
            buscarVeiculo(veiculos)
        elif opcao == 6:
            print("Saindo....")
            break
        else:
            print("Coloque uma opção válida")


if __name__ == '__main__':
    cadastrar_veiculos()