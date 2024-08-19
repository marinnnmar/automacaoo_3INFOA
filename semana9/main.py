import pyautogui
import time

def cadastrar(atleta, modalidade, medalha, comite):
    #Atleta
    cAtleta = pyautogui.locateCenterOnScreen('atleta.png', grayscale=True, confidence=0.7) #localizar
    pyautogui.click(cAtleta, duration=0.8) #clicar
    pyautogui.write(atleta) #digitar

    #Modalidade
    cModalidade = pyautogui.locateCenterOnScreen('modalidade.png', grayscale=True, confidence=0.8)
    pyautogui.click(cModalidade, duration=0.8)
    pyautogui.write(modalidade)

    #Medalha
    cMedalha = pyautogui.locateCenterOnScreen('medalha.png', grayscale=True, confidence=0.8)
    pyautogui.click(cMedalha, duration=0.8)
    pyautogui.write(medalha)

    #Comitê
    cComite = pyautogui.locateCenterOnScreen('comite.png', grayscale=True, confidence=0.8)
    pyautogui.click(cComite, duration=0.8)
    pyautogui.write(comite)

    #Enviar
    cEnviar = pyautogui.locateCenterOnScreen('salvar.png', grayscale=True, confidence=0.8)
    pyautogui.click(cEnviar, duration=0.8)

    time.sleep(2)

    #Enviar novamente
    cEnviarNovamente = pyautogui.locateCenterOnScreen('enviar_novamente.png', grayscale=True, confidence=0.8)
    pyautogui.click(cEnviarNovamente, duration=0.8)

    time.sleep(2)
