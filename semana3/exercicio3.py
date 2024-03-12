'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

contador = 1
grupo1 = []
grupo2 = []
grupo3 = []

while True:
    matricula = int(input('Digite a matrícula: '))
    if contador == 1:
        grupo1.append(matricula)
    elif contador == 2:
        grupo2.append(matricula)
    elif contador == 3:
        grupo3.append(matricula)
        contador = 1

    contador = contador + 1

    if matricula == 0:
        break
      
print("Grupo 1: ", grupo1)
print("Grupo 2: ", grupo2)
print("Grupo 3: ", grupo3)