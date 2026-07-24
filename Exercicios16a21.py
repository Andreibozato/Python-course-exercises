#Exercicio 16 - Um programa que leia um número Real qualquer  e mostre a sua porção Inteira.

nr = float(input("Digite um numero: "))
ni = (nr//1)
print("O numero {} tem a parte inteira \033[0;34m{}\033[m".format(nr,ni))

#Exercicio 17 - Um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e depois calcula e mostre o comprimento da hipotenusa.

co = int(input("Digite o cateto oposto: "))
ca = int(input("Digite o cateto adjacente: "))
h=(ca**2+co**2)**0.5
print("A hipotenusa é: \033[0;31m{:.2f}\033[m".format(h))

#Exercicio 18 - Um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang= float(input("Digite o valor do angulo: "))
seno = math.sin(math.radians(ang))//1
cos = math.cos(math.radians(ang))//1
tag = math.tan(math.radians(ang))//1
print("Do angulo {}, o seno é \033[0;33m{}\033[m, o cosseno é \033[0;32m{}\033[m e a tangente é \033[0;34m{}\033[m".format(ang,seno,cos,tag))

#Exercicio 19 e 20
#Exercicio 19 - Um programa que lê o nome dos alunos e escreve o nome do escolhido.


from random import choice

al1 = str(input("Digite o nome do primeiro aluno: "))
al2 = str(input("Digite o nome do segundo aluno: "))
al3 = str(input("Digite o nome do terceiro aluno: "))
al4 = str(input("Digite o nome do quarto aluno: "))
alunos = [al1,al2,al3,al4]
print("O aluno escolhido foi: \033[0;33m{}\033[m ". format(choice(alunos)))

#Exercicio 20 - Um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

shuffle(alunos)
print("A ordem de apresentação foi: \033[0;34m{}\033[m ".format(alunos))


#Exercicio 21 - Um programa que toca musica

import pygame
pygame.init()
pygame.mixer.music.load("house_lo.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)


