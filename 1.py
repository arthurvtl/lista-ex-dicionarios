def contar_vogais(texto):
    vogais = 'aeiou'
    texto = texto.lower()
    contagem_vogais = {}
    for vogal in vogais:
        contagem = texto.count(vogal)
        contagem_vogais[vogal] = contagem
    return contagem_vogais

texto = input('Insira o texto: ')
resultado = contar_vogais(texto)
print(resultado)