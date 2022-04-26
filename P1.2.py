# -*- coding: utf-8 -*-

"""
Faça um programa que leia vários intervalos abertos de inteiros. Para cada intervalo mostrar as quantidades de inteiros, 
de pares, de ímpares e de inteiros divisíveis por 5. Não ler o próximo intervalo caso, no intervalo atual, a quantidade de divisíveis por 5 for par.
"""

#fazendo a estrutura de repetição
while True:
    try:
        #qual variável buscar no início de cada repetição
        intervalos = input()
    except:
        #a condição para que a repetição pare
        if divcinco % 2 == 0:
            break

    #dividindo os dois valores pegos no início
    strA, strB = intervalos.split()

    #transformando os valores em inteiros
    A = int(strA)
    B = int(strB)

    #criando as variáveis que armazenarão os valores que serão mostrados no final do programa
    inteiros = 0
    pares = 0
    impares = 0
    divcinco = 0

    #criando a estrutura de repetição com o range dado pelos números pegos no início do programa
    for i in range(A+1,B):
        #calculando a quantidade de inteiros
        #checando se o número é zero
        if i == 0:
            #caso for não somar aos números inteiros
            inteiros += 0
        else:
            #caso não for zero somar aos números inteiros
            inteiros += 1

        #calculando a quantidade de números pares
        if i == 0:
            #caso o número for zero não adicionar à quantidade de pares
            pares += 0
        #checando se o número é par
        elif i % 2 == 0:
            #adicionando mais 1 na contagem de números pares
            pares += 1

        #calculando a quantidade de números impares
        if i == 0:
            #caso o número for 0 não adicionar à contagem
            impares += 0
        #checando se o número é ímpar
        elif i % 2 != 0:
            #adicionando mais 1 na contagem de números ímpares
            impares += 1

        #calculando se o número é divisível por 5
        if i == 0:
            #caso o número seja 0 não adicionar a contagem
            divcinco += 0
        #checando se é divisível por 5
        elif i % 5 == 0:
            #adicionando mais 1 à contagem caso seja divisível
            divcinco += 1

    #mostrar o intervalo
    print("Intervalo ({}, {}):".format(A,B))
    #mostrar a quantidade de inteiros
    print("Quantidade de inteiros: {}".format(inteiros))
    #mostrar a quantidade de pares
    print("Quantidade de pares: {}".format(pares))
    #mostrar a quantidade de ímpares
    print("Quantidade de ímpares: {}".format(impares))
    #mostrar a quantidade de divisíveis por 5
    print("Quantidade de divisíveis por 5: {}".format(divcinco))
    #checando se a quantidade de divisíveis por 5 é divisível por 2
    if divcinco % 2 != 0:
        #caso não seja, mostrar uma linha em branco
        print()

