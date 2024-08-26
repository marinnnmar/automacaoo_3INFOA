import time
import pyautogui
import pandas as pd



def cadastrar(Nome, Atividade, Nota):

    #Email
    cEmail = pyautogui.locateCenterOnScreen('email.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cEmail, duration=0.8) #clicar

    #Nome
    cNome = pyautogui.locateCenterOnScreen('nome_aluno.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cNome, duration=0.8) #clicar
    pyautogui.write(Nome) #digitar

    #Atividade
    cAtividade = pyautogui.locateCenterOnScreen('atividade_aluno.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cAtividade, duration=0.8) #clicar
    pyautogui.write(Atividade) #digitar

    #Nota
    cNota = pyautogui.locateCenterOnScreen('nota_aluno.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cNota, duration=0.8) #clicar
    pyautogui.write(str(Nota)) #digitar

    pyautogui.scroll(-300)

    #Turma
    cTurma = pyautogui.locateCenterOnScreen('turma_aluno.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cTurma, duration=0.8) #clicar

    #Enviar
    cEnviar = pyautogui.locateCenterOnScreen('enviar_aluno.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cEnviar, duration=0.8) #clicar

    time.sleep(2)

    #Enviar novamente
    cEnviarNovamente = pyautogui.locateCenterOnScreen('enviar_novamente_aluno.png', grayscale=True, confidence=0.8)
    pyautogui.click(cEnviarNovamente, duration=0.8)

    time.sleep(2)

