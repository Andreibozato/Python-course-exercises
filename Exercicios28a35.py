#Exercicio 28 - Um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from random import randint
from time import sleep

computador=randint(1,5)
print("-+="*30)
print("Vou pensar em um numéro entre 0 a 5")
print("-+="*30)
Jogador=int(input("Qual número eu pensei: "))
print("PROCESSANDO...")
sleep(2)
if computador == Jogador:
    print("\033[0;32mPARABÉNS, você acertou\033[m")
else:
    print("\033[0;31mGANHEI, você errou, eu pensei no numero {}\033[m".format(computador))

#Exercicio 29 - Um programa que leia a velocidade de um carro. (Caso ultrapassar 80Km/h, ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite).

kilometros=int(input("Qual a velocidade do carro: "))

if kilometros <= 80:
    print("\033[0;32mOk\033[m")
else:
    print("Você foi multado")
    multa = kilometros - 80
    print("Você pagara no total \033[0;31m{}\033[m reais".format(multa*7))

#Exercicio 30 - Um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n=int(input("Digite um numero: "))

if n%2==0:
    print("O numero é \033[0;33mpar\033[m")
else:
    print("O numero é \033[0;31mimpar\033[m")

#Exercicio 31 - Um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist=int(input("Qual a distância da viagem: "))
if dist<=200:
    print("Você pagará no total \033[0;32m{}\033[m reais".format(dist*0.5))
else:
    print("Você pagará no total \033[0;32m{}\033[m reais".format(dist*0.45))

#Exercicio 32 - Um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano=int(input("Que ano você quer analisar? Coloque 0 para analisar o ano atual: "))

if ano==0:
    ano = date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O ano de {} \033[0;32mé um ano bissexto\033[m".format(ano))
else:
    print("O ano de {} \033[0;31mnão é um ano bissexto\033[m".format(ano))

#Exercicio 33 - Um programa que leia três números e mostre qual é o maior e qual é o menor.

n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))
n3=int(input("Digite o terceiro numero: "))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1

if n1<n2 and n3<n2:
    maior = n2
if n1<n3 and n2<n3:
    maior = n3
print("O menor valor foi \033[0;31m{}\033[m".format(menor))
print("O maior valor foi \033[0;32m{}\033[m".format(maior))

#Exercicio 34 - Um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal=int(input("Qual o salário do trabalhador: "))
if sal > 1250:
    print("o novo salário será igual á \033[0;32m{}\033[m reais".format(sal+sal * 10 / 100))
else:
    print("o novo salário será igual á \033[0;32m{}\033[m reais".format(sal+sal * 15 / 100))

#Exercicio 35 - Um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1=int(input("Qual a primeira reta: "))
r2=int(input("Qual a segunda reta: "))
r3=int(input("Qual a terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Os segmentos \033[0;32mpodem formar\033[m um triângulo")
else:
    print("Os segmentos \033[0;31mnão podem formar\033[m um triângulo")

