"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).
"""

"""
A ideia geral do programa é usar uma estrutura de repetição (while) que se repetirá até um dos valores inputados ser igual ou menor que zero.
Nessa estrutura de repetição as strings inputadas serão convertidas em inteiros e o programa decidirá qual é a maior e qual é a menor dentre os dois inputs.
Depois disso o programa checará se os inputs são válidos para o programa continuar e criará uma estrutura de repetição utilizando o 'for' e 'range',
Dentro da estrutura de repetição final o programa imprime todos os valores de i na mesma linha com a separação de um espaço entre cada valor.
No final o programa imprime, também na mesma linha, a soma de todos esses valores.
"""

#equanto verdade
while True:
    #definindo variáveis que serão usadas
    #variável do menor
    menor = 0
    #variável do maior
    maior = 0
    #variável da soma que será imprimida no final
    soma = 0
    
    #dando os valores para M e N
    M, N = input().split()
    
    #transformando os valores de M e N em inteiros
    intM = int(M)
    intN = int(N)
    
    #checando se os valores são válidos para o programa continuar
    if intN <=0 or intM <= 0:
        break
    
    #checando qual dos valores é o maior, qual é o menor e os alocando em suas devidas variáveis
    if intM > intN:
        maior = intM
        menor = intN
    elif intN > intM:
        maior = intN
        menor = intM
      
    #estrutura de repetição do menor pro maior + 1  
    for i in range(menor,maior+1):
        #a soma dos números
        soma += i
        #imprimindo todos os valores de i
        print(i, end=" ")
    #imprimindo o valor da soma após os valores    
    print("Sum={}".format(soma))
            