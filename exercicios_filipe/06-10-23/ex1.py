import datetime
def validade():
    fabricacao_str = input('Data de fabricação: ')
    fabricacao = datetime.datetime.strptime(fabricacao_str, '')

    prazo_em_dias = int(input('Prazo de validade em dias: '))
    intervalo_validade = datetime.timedelta(day=prazo_em_dias)

    data_de_validade = fabricacao + intervalo_validade
    
    print(data_de_validade)

if __name__ == '__main__':
    validade()