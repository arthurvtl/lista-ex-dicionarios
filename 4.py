agenda = {}

def incluirNovoNome():
    nome = input('Insira o nome: ')
    telefones = []
    while True:
        telefone = input('Insira um telefone (ou "fim" para encerrar): ')
        if telefone == 'fim':
            break
        telefones.append(telefone)
    agenda[nome] = telefones

def incluirTelefone():
    nome = input('Insira o nome: ')
    if nome in agenda:
        telefone = input('Insira o telefone: ')
        agenda[nome].append(telefone)
    else:
        resposta = input('O nome {} não existe na agenda. Deseja incluí-lo? (s/n) '.format(nome))
        if resposta.lower() == 's':
            telefones = []
            while True:
                telefone = input('Insira um telefone (ou "fim" para encerrar): ')
                if telefone == 'fim':
                    break
                telefones.append(telefone)
            agenda[nome] = telefones

def excluirTelefone():
    nome = input('Insira o nome: ')
    if nome in agenda:
        telefone = input('Insira o telefone: ')
        agenda[nome].remove(telefone)
        if len(agenda[nome]) == 0:
            del agenda[nome]

def excluirNome():
    nome = input('Insira o nome: ')
    if nome in agenda:
        del agenda[nome]

def consultarTelefone():
    nome = input('Insira o nome: ')
    if nome in agenda:
        print('Telefones de {}: {}'.format(nome,agenda[nome]))
    else:
        print('O nome {} não existe na agenda.'.format(nome))

while True:
    opcao = input('Escolha uma opção: \n1 - Incluir novo nome\n2 - Incluir telefone\n3 - Excluir telefone\n4 - Excluir nome\n5 - Consultar telefone\n6 - Sair\nOpção: ')
    if opcao == '1':
        incluirNovoNome()
    elif opcao == '2':
        incluirTelefone()
    elif opcao == '3':
        excluirTelefone()
    elif opcao == '4':
        excluirNome()
    elif opcao == '5':
        consultarTelefone()
    elif opcao == '6':
        break