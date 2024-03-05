'''
Exercício 1:
 Crie um programa que lê dois número
 inteiros do teclado e após imprime 
 o maior números dentre eles.
'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(num1, "é o maior")
elif num2 > num1:
    print(num2, "é o maior")
else:
    print("Os dois números são iguais")