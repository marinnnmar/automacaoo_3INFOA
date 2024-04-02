'''
Crie um programa que imprime uma tabuada. O programa deve solicitar
que o usuário informe um número para gerar a tabuada. Utilizando um
laço de repetição, o programa deve gerar a tabuada do número
fornecido de 0 a 100.
'''

num = int (input("Informe um número: "))

for i in range(0, 101):
    resultado = i*num
    print(num, "X", i, "=", resultado)