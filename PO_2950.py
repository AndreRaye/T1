"""
Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. 
Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar,
um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron).
Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais.
Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente.
Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM).
Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que
para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos.
Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, 
querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.

Entrada
A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100)
Que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.
"""

"""
A ideia do programa é simples, pegar os três inputs do usuário como números inteiros e realizar o cálculo do ICM que é dividir o primeiro input pela soma dos dois últimos
Após isso é só printar o resultado com a precisão de duas casas decimais.
"""

#pegando os três inputs do usuário e os colocando em suas variáveis
Nstr, Xstr, Ystr = input().split()

#transformando os inputs do usuário em inteiros
N = int(Nstr)
X = int(Xstr)
Y = int(Ystr)

#definindo a soma entre os dois diâmetros
sd = X + Y
#definindo o ICM
ICM = N / sd

#imprimindo o resultado com precisão de duas casas decimais
print("{:.2f}".format(ICM))