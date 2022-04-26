# -*- coding: utf-8 -*-

"""
Fazer um programa que leia vários casos de teste, terminados com fim de arquivo (EOF). 
Cada caso de teste corresponde a uma leitura de 10 números inteiros, com definição pelo programa de qual é o menor número lido, x;
seguida de uma leitura de 10 números inteiros, com definição pelo programa de qual é o maior número lido, y. 
O programa deverá mostrar a média, com uma casa decimal, dos valores inteiros entre x e y, incluindo x e y.
"""

#criando a estrutura de repetição que fará o programa
while True:
    #mostrando o que a estrutura de repetição fará
    try:
        #criando variáveis que serão usadas no programa
        menor = 99999
        maior = -99999
        #criando o contador que será usado na média final
        cont = 0
        #criando a soma que será usada na média final
        soma = 0
        #criando a auxiliar que será utilizada no programa
        aux = 0
        
        #criando a primeira estrutura de repetição que achará o número mínimo
        for i in range(1,11):
            #pedindo o input de um número inteiro do usuário
            N1 = int(input())
            #checando se o input do usuário é menor que a variável menor
            if N1 < menor:
                #transformando a variável menor no input do usuário
                menor = N1
        #criando a estrutura de repetição que achará o número maior
        for i in range(1,11):
            #pedindo o input de um número inteiro ao usuário
            N2 = int(input())
            #checando se o input do usuário é maior que a variável maior
            if N2 > maior:
                #transformando a maior no input do usuário
                maior = N2
        #checando qual variável é a maior
        if menor > maior:
            #transformando a maior na auxiliar
            aux = maior
            #transformando a maior na menor
            maior = menor
            #transformando a menor na auxiliar
            menor = aux
        #fazendo a estrutura de repetição da média
        for i in range(menor, maior+1):
            #usando o contador de termos
            cont += 1
            #fazendo a soma de todos os termos
            soma = soma + i
        #calculando a média final
        final = soma/cont
        #mostrando a média final com uma casa decimal após a vírgula
        print("{:.1f}".format(final))
    except EOFError:
        break

