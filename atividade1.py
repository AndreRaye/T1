"""
Faça um programa que leia 5 códigos de curso de 5 estudantes da UFMS.
Então conte quantos códigos são da Faculdade de Computação - Facom, quantos códigos são do Instituto de Matemática - Inma e quantos são de outras unidades.
Mostre o resultado da contabilização. 
Os códigos dos cursos da Facom são: 1902: Análise e Desenvolvimento de Sistemas - Tecnologia; 1904: Ciência da Computação - Bacharelado;
1905: Engenharia de Computação - Bacharelado; 1906: Engenharia de Software - Bacharelado; 1907: Sistemas de Informação - Bacharelado.
Os códigos de cursos do Inma são: 2201: Matemática - Licenciatura (Integral); 2202: Matemática - Licenciatura (Noturno); 2203: Matemática - Bacharelado (Matutino);
 2291: Matemática - Licenciatura (A distância).
 """
 #input que armazenará as os valores dos cursos nas variáveis
strA, strB, strC, strD, strE = input().split()

#transformando as variáveis strings em inteiros
A = int(strA)
B = int(strB)
C = int(strC)
D = int(strD)
E = int(strE)

#variáveis nas quais serão armazenadas as quantidades de estudantes nas unidades
f = 0
i = 0
oi = 0

#condicional que dirá quantos estudantes são da FACOM
if A == 1902 or A == 1904 or A == 1905 or A == 1906 or A == 1907:
    f = f + 1
if B == 1902 or B == 1904 or B == 1905 or B == 1906 or B == 1907:
    f = f + 1
if C == 1902 or C == 1904 or C == 1905 or C == 1906 or C == 1907:
    f = f + 1
if D == 1902 or D == 1904 or D == 1905 or D == 1906 or D == 1907:
    f = f + 1
if E == 1902 or E == 1904 or E == 1905 or E == 1906 or E == 1907:
    f = f + 1

#condicional que dirá quantos estudantes são da INMA
if A == 2201 or A == 2202 or A == 2203 or A == 2291:
    i = i + 1
if B == 2201 or B == 2202 or B == 2203 or B == 2291:
    i = i + 1
if C == 2201 or C == 2202 or C == 2203 or C == 2291:
    i = i + 1
if D == 2201 or D == 2202 or D == 2203 or D == 2291:
    i = i + 1
if E == 2201 or E == 2202 or E == 2203 or E == 2291:
    i = i + 1

#condicional que dirá quantos estudantes são de outras instituições
if A != 1902 and A != 1904 and A != 1905 and A != 1906 and A != 1907 and A != 2201 and A != 2202 and A != 2203 and A != 2291:
    oi = oi + 1
if B != 1902 and B != 1904 and B != 1905 and B != 1906 and B != 1907 and B != 2201 and B != 2202 and B != 2203 and B != 2291:
    oi = oi + 1
if C != 1902 and C != 1904 and C != 1905 and C != 1906 and C != 1907 and C != 2201 and C != 2202 and C != 2203 and C != 2291:
    oi = oi + 1
if D != 1902 and D != 1904 and D != 1905 and D != 1906 and D != 1907 and D != 2201 and D != 2202 and D != 2203 and D != 2291:
    oi = oi + 1
if E != 1902 and E != 1904 and E != 1905 and E != 1906 and E != 1907 and E != 2201 and E != 2202 and E != 2203 and E != 2291:
    oi = oi + 1

#mostrar quantos estudantes são de quais locais
print("Facom: " + str(f))
print("Inma: " + str(i))
print("Outras unidades: " + str(oi))