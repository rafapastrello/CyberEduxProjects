qtd = int(input("\nInforme quantos alunos irá cadastrar: "))

soma_medias = 0
aluno_maior_nota = 0
media_geral = 0
maior_nota = 0
aprovados = 0
reprovados = 0
i = 1

for i in range(1, qtd + 1):

    nota1 = nota2 = nota3 = nota4 = -1

    print(f"===== ALUNO {i} =====")

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input(f"Insira a primeira nota do aluno {i} (0-10): "))

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input(f"Insira a segunda nota do aluno {i} (0-10): "))

    while nota3 < 0 or nota3 > 10:
        nota3 = float(input(f"Insira a terceira nota do aluno {i} (0-10): "))

    while nota4 < 0 or nota4 > 10:
        nota4 = float(input(f"Insira a quarta nota do aluno {i} (0-10): "))

    if nota1 > maior_nota:
        maior_nota = nota1
        aluno_maior_nota = i

    if nota2 > maior_nota:
        maior_nota = nota2
        aluno_maior_nota = i

    if nota3 > maior_nota:
        maior_nota = nota3
        aluno_maior_nota = i

    if nota4 > maior_nota:
        maior_nota = nota4
        aluno_maior_nota = i

    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4
    soma_medias = soma_medias + media

    if media >= 9:
        conceito = 'A'

    elif media >= 7 and media < 9:
        conceito = 'B'

    elif media >= 6 and media < 7:
        conceito = 'C'

    else:
        conceito = 'D'

    if conceito == 'D':
        situacao = 'Reprovado'
        reprovados += 1

    else:
        situacao = 'Aprovado'

    print('-------------------------------')
    print(f'Aluno {i}:')
    print(f'Média ------ {media}')
    print(f'Conceito --- {conceito}')
    print(f'Situação --- {situacao}')
    print('-------------------------------')

print('===== RELATÓRIO DA TURMA =====')
print(f'A maior nota foi {maior_nota}, do aluno {aluno_maior_nota} ')
print(f'A média da turma foi {soma_medias / qtd}')
print(f'A turma teve {reprovados} alunos reprovados.')