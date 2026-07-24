#Exercicio 22 - Um programa que leia o nome completo de uma pessoa e mostre: – O nome com todas as letras maiúsculas e minúsculas; – Quantas letras ao todo (sem considerar espaços); – Quantas letras tem o primeiro nome.

nome= input("Digite seu nome completo: ")

print("Nome em letra maiúscula: \033[0;31m{}\033[m ".format(nome.upper()))
print("Nome em letra minúscula: \033[0;33m{}\033[m ".format(nome.lower()))
print("Seu nome possui \033[0;34m{}\033[m letras n total".format(len(nome.replace(" ", ""))))
dividido = nome.split()
print("Seu primeiro nome tem \033[0;35m{}\033[m letras".format(len(dividido[0])))

#Exercicio 23 - Um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num= int(input("Digite a senha (de 0 a 9999): "))
u= num//1%10
d= num//10%10
c= num//100%10
m= num//1000
print("\033[0;31mUnidade: {}\033[m".format(u))
print("\033[0;33mDezena: {}\033[m".format(d))
print("\033[0;32mCentena: {}\033[m".format(c))
print("\033[0;34mMilhar: {}\033[m".format(m))

#Exercicio 24 - Um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite sua cidade: "))

print("A sua cidade possui a palavra 'Santo'? \033[0;31m{}\033[m".format(cidade[:5].upper()=="SANTO"))

#Exercicio 25 - Um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome2= input("Digite seu nome completo: ")

print("O seu nome possui 'Silva' no nome? \033[0;31m{}\033[m ".format("silva" in nome2.lower()))

#Exercicio 26 - Um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

fr=str(input("Digite uma frase: "))

fr = fr.upper()
print("Aparaceu a letra A {} vezes".format(fr.count("A")))
print("A letra A aparece pela primeira vez na posição \033[0;33m{}\033[m".format((fr.find("A"))+1))
print("A letra A aparece pela ultima vez na posição \033[0;34m{}\033[m".format((fr.rfind("A"))+1))

#Exercicio 27 - Um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome3= input("Digite seu nome completo: ")

dividido2 = nome3.split()
print("Seu primeiro nome é: \033[0;31m{}\033[m".format(dividido2[0]))
print("Seu ultimo nome é \033[0;34m{}\033[m".format(dividido2[len(dividido2)-1]))