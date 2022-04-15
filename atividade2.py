"""
Faça um programa que leia um número inteiro N (-1 < N < 10000), 
e mostre quantos milhares, centenas, dezenas e unidades esse número possui.
"""

#o numero a ser calculado
N = int(input())

#calcular o valor posicional das casas decimais
U = N // 1 % 10
D = N // 10 % 10
C = N // 100 % 10
M = N // 1000 % 10

#mostrar o número e seus valores posicionais
print(N)
print(str(M) + " milhar(es)")
print(str(C) + " centena(s)") 
print(str(D) + " dezena(s)")
print(str(U) + " unidade(s)")