notas = {}
while True:
    nome = input('Insira o nome do aluno (ou "fim" para encerrar): ')
    if nome == 'fim':
        break
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    notas[nome] = [nota1, nota2]

medias = {}
for nome, notas_aluno in notas.items():
    media = sum(notas_aluno) / len(notas_aluno)
    medias[nome] = media

reprovados = 0
recuperacao = 0
aprovados = 0
for media in medias.values():
    if media < 5:
        reprovados += 1
    elif media < 7:
        recuperacao += 1
    else:
        aprovados += 1

print(f'Alunos reprovados: {reprovados}')
print(f'Alunos de recuperação: {recuperacao}')
print(f'Alunos aprovados: {aprovados}')