       Questão 01

INDICE = 13
SOMA = 0
K = 0 

while K < INDICE:
    K = K+1
    SOMA = SOMA+K

print(f'{SOMA}')

Ao final, o valor da variável SOMA será: 91



       Questão 02

def verific_f(num):
    a, b = 0, 1

    while a <= num:
        if b == num:
            return True
        a, b = b, a+b
    return False

num_info = 21

if verific_f(num_info):
    print(f'{num_info} Pertence à sequência de Fibonacci')
else:
    print(f'{num_info} Não pertence a sequência de Fibonacci')




       Questão 03

1, 3, 5, 7, 9
2, 4, 8, 16, 32, 64, 128
0, 1, 4, 9, 16, 25, 36, 49
4, 16, 36, 64, 100
1, 1, 2, 3, 5, 8, 13
2, 10, 12, 16, 17, 18, 19, 22




       Questão 04

Eu ligaria o primeiro interruptor e deixaria ele por um tempo ligado, para esquentar a lâmpada.
Depois eu desligaria o primeiro interruptor e ligaria o segundo.
Iria até uma das salas conferir se a lâmpada está acessa ou quente.
Se a lâmpada estiver quente, ela pertence ao primeiro interruptor, se estiver ligada, pertence ao segundo Interruptor.
E por fim, se a lâmpada estiver fria e desligada, pertence ao terceiro interruptor.




       Questão 05

def invert_string(original):
    invert = ""

    for char in original[::-1]:
        invert += char
    return invert

comando_usu = input('Digite algo: ')
result = invert_string(comando_usu)

print(f'Invertida: {result}')
