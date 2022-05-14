"""
Nick é um cientista que viaja por diversos universos paralelos, juntamente com o seu neto, Mory.
Em um desses universos, havia um programa de televisão, que premiava quem adivinhasse as alturas máximas de arremessos de frutas. 
Neste local, a massa da fruta não influenciava na altura máxima do arremesso.
Nick calculava o ângulo do arremesso, que formava sempre uma parábola, e extraía uma função de segundo grau da trajetória.
Ajude Nick e Mory a ganhar muitos prêmios neste programa.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro T (2 <= T <= 99) relativo ao número de casos de teste.
As T linhas seguintes possuem três valores inteiros
A (A < 0), B e C (-100 <= B, C <= 100), representando os coeficientes de uma função de segundo grau, na forma ax2 + bx + c.

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número real, com aproximação de duas casas decimais,
a altura máxima do arremesso de uma fruta.
"""

"""
A ideia do programa é criar uma estrutura de repetição do tamanho dado pelo input inicial do usuário e fazer o cálculo dentro dessa estrutura de repetição.
Dentro da estrutura de repetição o programa transforma os inputs de A, B e C do usuário em inteiros e faz o calculo de X com isso que será usado no cálculo da altura.
Após isso é feito o cálculo da altura e é imprimido para o usuário com precisão de duas casas decimais.
"""

#pegando o input de número inteiro do usuário T
T = int(input())

#criando a estrutura de repetição de tamanho T
for i in range(T):
    #pegando os inputs do usuário Astr, Bstr, Cstr
    Astr, Bstr, Cstr = input().split()
    
    #transformando os inputs em inteiros
    A = int(Astr)
    B = int(Bstr)
    C = int(Cstr)
    
    #fazendo o cálculo de X a partir dos inputs do usuário
    X = -(B/(2*A))
    #fazendo o cálculo da altura máxima utilizando o X e os inputs do usuário
    altura = (A * (X**2)) + (B * X) + C
    
    #imprimindo para o usuário a altura máxima com precisão de duas casas decimais
    print("{:.2f}".format(altura))