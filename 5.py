import datetime

def maior_de_18(dataNasc):
    data = datetime.datetime.now()
    anoAtual = data.year
    mesAtual = data.month
    diaAtual = data.day
    anoNasc, mesNasc, diaNasc = map(int, dataNasc.split('/'))
    if anoAtual - anoNasc > 18:
        return True
    elif anoAtual - anoNasc == 18 and mesAtual > mesNasc:
        return True
    elif mesAtual == mesNasc and diaAtual >= diaNasc:
        return True
    else:
        return False

pessoas = {}
while True:
    nome = input('Insira o nome (ou "fim" para encerrar): ')
    if nome == 'fim':
        break
    dataNasc = input('Insira a data de nascimento (formato DD/MM/AAAA): ')
    cpf = input('Insira o CPF: ')
    pessoas[nome] = {'dataNasc': dataNasc, 'cpf': cpf}

maiores = {}
menores = {}
for nome, dados in pessoas.items():
    if maior_de_18(dados["dataNasc"]):
        maiores[nome] = dados
    else:
        menores[nome] = dados

print('Pessoas maiores de 18 anos:')
for nome, dados in maiores.items():
    print('Nome: {}, Data de nascimento: {}, CPF: {}'.format(nome,dados["dataNasc"],dados["cpf"]))

print('Pessoas menores de 18 anos:')
for nome, dados in menores.items():
    print('Nome: {}, Data de nascimento: {}, CPF: {}'.format(nome,dados["dataNasc"],dados["cpf"]))