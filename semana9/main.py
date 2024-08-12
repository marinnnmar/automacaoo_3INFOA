import pyautogui

#Atleta
cAtleta = pyautogui.locateCenterOnScreen('atleta.png', grayscale=True, confidence=0.8) #localizar
pyautogui.click(cAtleta, duration=0.8) #clicar
pyautogui.write('Novo Atleta') #digitar

#Modalidade
cModalidade = pyautogui.locateCenterOnScreen('modalidade.png', grayscale=True, confidence=0.8)
pyautogui.click(cModalidade, duration=0.8)
pyautogui.write('Nova Modalidade')

#Medalha
cMedalha = pyautogui.locateCenterOnScreen('medalha.png', grayscale=True, confidence=0.8)
pyautogui.click(cMedalha, duration=0.8)
pyautogui.write('Ouro')

#Comitê
cComite = pyautogui.locateCenterOnScreen('comite.png', grayscale=True, confidence=0.8)
pyautogui.click(cComite, duration=0.8)
pyautogui.write('Brasil')

#Enviar
cEnviar = pyautogui.locateCenterOnScreen('salvar.png', grayscale=True, confidence=0.8)
pyautogui.click(cEnviar, duration=0.8)