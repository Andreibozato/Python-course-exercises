from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from tkinter.filedialog import dialogstates

#Exercicio 5 - Programa que lê um número inteiro e mostra seu antecessor e sucessor:

n = int(input("Digite um numero: "))
a = n - 1
d = n + 1
print("\033[0;31mAntecessor: {}\033[m,\033[0;33m Atual: {}\033[m,\033[0;32m Sucessor: {}\033[m".format(a,n,d))

#Exercicio 6 - Programa que lê um número e mostre o seu dobro, triplo e raiz quadrada:

n = int(input("Digite um numero: "))
db = n*2
tr = n*3
rq = n**0.5
print("o Dobro de {} é \033[0;31m{}\033[m, o Triplo é \033[0;33m{}\033[m e a Raiz Quadrada é \033[0;32m{:.2f}\033[m".format (n,db,tr,rq))

#Exercicio 7 - Programa que lê duas notas de um aluno e calcula a sua média:

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
m = (nota1+nota2)/2
print("A média do aluno foi de \033[0;32m{}\033[m".format(m))

#Exercicio 8 - Programa que converte o valor em metros para centrimetros e milimetros:

metros= int(input("Quantos metros:? "))
cent= metros * 100
mili = metros * 1000
print("Em centimetro: \033[0;33m{}\033[m, em milimetros: \033[0;34m{}\033[m".format(cent,mili))

#Exercicio 9 - Programa que mostra a tabuada de um número:

n = int(input("Digite um numero: "))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,1,n*1))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,2,n*2))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,3,n*3))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,4,n*4))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,5,n*5))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,6,n*6))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,7,n*7))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,8,n*8))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,9,n*9))
print("O valor {} x {} = \033[0;35m{}\033[m: ".format(n,10,n*10))

#Exercicio 10 - Conversão de Reais para Dólares:

din = int(input("Quantos reais você tem? "))
dol = din//3.27
print("Voce pode ter \033[0;32m{}\033[m dolares".format (dol))

#Exercicio 11 - Programa que calcula a área (com a largura e altura) e a quantidade de tinta necessária para pintá-la (cada litro de tinta pinta uma área de 2 metros quadrados):

lar = int(input("Qual a largura da estrutura: "))
altu = int(input("E a altura? "))
area = lar*altu
tinta = area//2
print("A ârea foi de \033[0;34m{}\033[m metros cubicos e foi necessario \033[0;35m{}\033[m litros de tinta".format(area,tinta))

#Exercicio 12 - Programa que coloca um preço novo com desconto:

preco=int(input("Qual o preço? "))
desc = preco-(preco*5/100)
print("O valor do novo preço é de \033[0;32m{}\033[m reais".format(desc))

#Exercicio 13 - Programa que aumenta um sálario em 15%:

sal=int(input("Qual o salario? "))
nsal = sal+(sal*15/100)
print("O valor do novo salario é de \033[0;32m{}\033[m reais".format(nsal))

#Exercicio 14 -

C= int(input("Qual a temperatura em Celsius? "))
F= (C*9/5)+32
print("Em fahrenheit é \033[0;34m{}\033[m graus".format(F))

#Exercicio 15

Km=int(input("Quantos kilometros foram percorridos: "))
dia=int(input("A quantos dias o carro foi alugado: "))
total=(Km*0.15)+(dia*60)
print("O valor total foi de \033[0;32m{}\033[m reais".format(total))