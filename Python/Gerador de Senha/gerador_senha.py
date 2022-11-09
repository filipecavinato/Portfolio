import random

def gerarSenha(tamanho):
    caracter = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    numero = "0123456789"
    caracterEspecial = "!@#$%&*_"
    senha = ''

    while len(senha) < tamanho:
        if len(senha) < (tamanho - 2):
            senha += caracter[random.randint(0, len(caracter) - 1)]
        elif len(senha) < (tamanho - 1):
            senha += str(numero[random.randint(0, len(numero) - 1)])
        else:
            senha += caracterEspecial[random.randint(0, len(caracterEspecial) - 1)]
    return senha

print('----Gerador de Senhas----')
tamanho = int(input('Deseja uma senha com quantos caracteres: '))
senha = gerarSenha(tamanho)
print(f'Sua senha é: {senha}')