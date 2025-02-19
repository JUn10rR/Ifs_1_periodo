import random
def aleatorio():
    numero = random.uniform(0.0, 10.0)

a = aleatorio()
b = aleatorio()
c = aleatorio()
d = aleatorio()


def soma(a, b, c, d):
    return a, b, c, d

def media(a, b, c, d):
    return (a, b, c, d)

def maior_nota(a, b, c, d):
    return max(a, b, c, d)

def menor_nota(a, b, c, d):
    return min(a, b, c, d)

resul_soma = soma(a, b, c, d)
resul_media = media(a, b, c, d)
resul_maior = maior_nota(a, b, c, d)
resul_menor = menor_nota(a, b, c, d)

print(f'A soma é: {resul_soma:.2f}')
print(f'A média é: {resul_media:.2f}')
print(f'O maior é: {resul_maior:.2f}')
print(f'O menor é: {resul_menor:.2f}')