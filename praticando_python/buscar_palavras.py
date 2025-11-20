import os

os.system ('cls')

def buscar_palavras (texto_digitado):
    encontradas = []
    palavras_separadas = texto_digitado.split()
    for palavra in palavras_separadas:
        if len(palavra) > 10:
            encontradas.append(palavra)
    return encontradas

print('Vamos verificar quantas palavras longas preenchem seu texto')

texto_digitado = input(f'Digite um texto: ')

palavras_longas = buscar_palavras(texto_digitado)

if palavras_longas:
    print('Palavras longas encontradas: ')
    for palavra in palavras_longas:
        print(palavra)
else:
    print('Nenhuma palavra longa foi encontrada no texto')

