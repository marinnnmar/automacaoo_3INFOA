'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

matriculas = []
while True:
    matricula = int(input("Digite a matrícula: "))
    matriculas.append(matricula)
    if matricula == 0:
        print(matriculas)
        break