import pyautogui, time

#clica no campo de login
pyautogui.moveTo(360, 500, duration=.5)

pyautogui.write('mariana.marcilio@alunos.ifsuldeminas.edu.br', interval=0.1)

#clica no botão avançar
pyautogui.click(640, 750, duration=1)

time.sleep(10)

pyautogui.write("nao nao nao", interval=0.1)

pyautogui.click(262, 607, duration=1)
pyautogui.click(635, 749, duration=10)
