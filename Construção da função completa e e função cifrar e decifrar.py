# Construção da função completa passo a passo com código anteriormente definido
def cesar(texto, deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    tabela_de_traducao = str.maketrans(alfabeto, alfabeto_deslocado)
    texto_cifrado = texto.translate(tabela_de_traducao)
    return texto_cifrado

#Acima, a função cesar criptografa o texto fornecido com o deslocamento especificado, porém não lida com letras maiúsculas. Para mudar isso:
# Adicionamos o alfabeto maiusculo à tabela de tradução, com concatenação das respectivas variaveis em maiusculo:

def cesar(texto, deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    tabela_de_traducao = str.maketrans(alfabeto + alfabeto.upper(), alfabeto_deslocado + alfabeto_deslocado.upper())
    texto_cifrado = texto.translate(tabela_de_traducao)
    return texto_cifrado

# Agora, precisamos adicionar validações, garantindo que apenas números inteiros façam parte do deslocamento, e que o deslocamento esteja entre 1 e 25:

def cesar(texto, deslocamento):
    if not isinstance(deslocamento, int):
        return 'Erro: o deslocamento deve ser um número inteiro.'
    if deslocamento < 1 or deslocamento > 25:
        return 'Erro: o deslocamento deve estar entre 1 e 25.'
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    tabela_de_traducao = str.maketrans(alfabeto + alfabeto.upper(), alfabeto_deslocado + alfabeto_deslocado.upper())
    texto_cifrado = texto.translate(tabela_de_traducao)
    return texto_cifrado

# Python permite estabelecer parâmetros padrão para funções. Assim, podemos definir um terceiro parâmetro chamado 'cifrar'.
# Esse parâmetro "cifrar" indicará se o texto deve ser cifrado ou decifrado.
# Por padrão, definimos "cifrar" como true, o que significa que o texto será cifrado.
#Se "cifrar" for False, o texto será decifrado. Obs: Cifrar será False se o parâmetro for omitido.
# Note também que vamos criar duas funções de cesar no final, uma cifra e outra decifra, graças à lógica do parâmetro "cifrar".

def cesar(texto, deslocamento, cifrar=True):
    if not isinstance(deslocamento, int):
        return 'Erro: o deslocamento deve ser um número inteiro.'
    if deslocamento < 1 or deslocamento > 25:
        return 'Erro: o deslocamento deve estar entre 1 e 25.'
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
     if not cifrar:
       deslocamento = -deslocamento
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    tabela_de_traducao = str.maketrans(alfabeto + alfabeto.upper(), alfabeto_deslocado + alfabeto_deslocado.upper())
    texto_cifrado = texto.translate(tabela_de_traducao)
    return texto_cifrado
def cifrar(texto, deslocamento):
    return cesar(texto, deslocamento)
def decifrar(texto, deslocamento):
    return cesar(texto, deslocamento, cifrar=False)

# Agora, podemos testar as funções cifrar e decifrar:
cifrar('Aqui esta uma FRASE para ser cifrada como exemplo, usando tanto caracteres MAIUSCULOS quanto minusculos!', 4) 
#output: 'Eyum wxwe yqei JVWEI tets wiv gmhvehi gsqi ihqtso, ywsri wexrs gewxivwgi QEMWYGWQSY geqwi qmrwgyqs!'
decifrar('Eyum wxwe yqei JVWEI tets wiv gmhvehi gsqi ihqtso, ywsri wexrs gewxivwgi QEMWYGWQSY geqwi qmrwgyqs!', 4)
#output: 'Aqui esta uma FRASE para ser cifrada como exemplo, usando tanto caracteres MAIUSCULOS quanto minusculos!'



