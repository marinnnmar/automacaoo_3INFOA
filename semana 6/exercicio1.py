'''
Fazer uma pesquisa no google
Clique no campo de pesquisa, após digite o texto "como automatizar o whatsapp" após, pressione a tecla enter
'''

import pyautogui

pyautogui.click(351, 412, duration=0.2)
pyautogui.write('como automatizar o whatsapp', interval=0.2)
pyautogui.press('enter')

pyautogui.moveTo(24, 338, duration=.5)
pyautogui.dragRel(370, 133, duration=.5)

pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1006, 631, duration=.5)
pyautogui.hotkey('ctrl', 'v')


