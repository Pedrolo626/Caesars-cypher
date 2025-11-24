#Versão básica de cifra de César em Python
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
deslocamento = 6
alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
tabela_de_traducao = str.maketrans(alfabeto, alfabeto_deslocado)
texto = 'ola, mundo'
texto_cifrado = texto.translate(tabela_de_traducao)
print(texto_cifrado)