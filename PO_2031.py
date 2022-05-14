"""
Pedra, Papel, Ataque Aéreo é um jogo infantil muito popular, em que duas ou mais crianças formam um círculo e fazem gestos com a mão na tentativa de obter a vitória.
As regras são surpreendentemente complexas para um jogo de crianças, mas mesmo assim é bastante popular por todo o mundo.

As partidas são muito simples. Os jogadores podem escolher entre o sinal de uma Pedra (o punho), o sinal de um Papel (a palma aberta),
e o sinal para o Ataque Aéreo (igual o do Papel, mas com apenas o polegar e o mindinho estendidos).

Uma partida, com dois jogadores, possuem as seguintes regras para se definir um vencedor:

Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.
Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.
Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.
Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.
Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.
Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.
Sua tarefa é escrever um programa que, dada as escolhas de dois jogadores, informe quem venceu o jogo.
"""

"""
A ideia do exercício é criar uma estrutura de repetição com o tamanho dado pelo usuário com seu primeiro input e ao final de cada repetição imprimir o resultado do jogo.
Cada vez que a repetição chegar ao fim ela mostrará ao usuário um resultado final dado pelos seus inputs dentro da repetição.
Pra começar se pega um inteiro que será o tamanho do caso de testes/jogos da repetição.
Após isso é criada a estrutura de repetição, dentro dessa estrutura pegaremos duas strings que servirão como jogador1 e jogador2.
Essas duas strings passarão por condições if e elif para checar qual o resultado.
"""

#pegando o inteiro que será o tamanho da estrutura de repetição
N = int(input())

#criando a repetição de range N
for i in range(N):
    #string do jogador 1
    p1 = input()
    #string do jogador 2
    p2 = input()
    
    #condições if e elif para checar qual o resultado
    #checando se o resultado é aniquilação mútua
    if p1 == "ataque" and p2 == "ataque":
        #imprimindo o resultado
        print("Aniquilacao mutua")
    #checando se o jogador 1 venceu por ter usado ataque aéreo
    elif p1 == "ataque":
        #imprimindo o resultado
        print("Jogador 1 venceu")
    #checando se o jogador 2 venceu por ter usado ataque aéreo
    elif p2 == "ataque":
        #imprimindo o resultado
        print("Jogador 2 venceu")
    #checando se o jogador 1 venceu por ter usado pedra contra papel
    elif p1 == "pedra" and p2 == "papel":
        #imprimindo o resultado
        print("Jogador 1 venceu")
    #checando se o jogador 2 venceu por ter usado pedra contra papel
    elif p2 == "pedra" and p1 == "papel":
        #imprimindo o resultado
        print("Jogador 2 venceu")
    #checando se os dois jogadores venceram por terem usado papel contra papel
    elif p1 == "papel" and p2 == "papel":
        #imprimindo o resultado
        print("Ambos venceram")
    #checando se ninguém venceu caso os dois tenham usado pedra
    elif p1 == "pedra" and p2 == "pedra":
        #imprimindo o resultado
        print("Sem ganhador")