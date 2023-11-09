import os

def salvar_lista(lista):
    f = open('cadastros.txt', 'w')
    f.write(str(lista))
    f.close()

def ler_lista():
    if not os.path.exists('cadastros.txt'):
        salvar_lista([])
    f = open('cadastros.txt', 'r')
    text = f.read()
    lista = eval(text)
    return lista

def cadastrar(lista):
    nome = input('Nome: ')
    lista.append(nome)
    salvar_lista(lista)

def listar(lista):
    for nome in lista:
        print(nome)

def menu(lista):
    print('1 - cadastrar nome\n2 - listar cadastros')
    opcao = input('Digite a opção: ')
    if opcao == '1':
        cadastrar(lista)
    elif opcao == '2':
        listar(lista)
    else:
        print('Opção inválida')

if __name__ == '__main__':
    lista = ler_lista()
    while True:
        menu(lista)