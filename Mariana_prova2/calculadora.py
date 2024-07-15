'''Nessa atividade prática, você deve criar um programa em Python que abra
o aplicativo de calculadora do Windows. Após abrir a calculadora, faça o
ponteiro do mouse clicar nos botões "7", "X", "7", e depois pressione a tecla "="
do teclado.
'''

import pyautogui

pyautogui.click(810,1056, duration=.5)
pyautogui.write('calculadora', interval=0.2)
pyautogui.click(850,430, duration=.5)

pyautogui.click(90,378, duration=.5)
pyautogui.click(325,378, duration=.5)
pyautogui.click(90,378, duration=.5)
pyautogui.press('=')