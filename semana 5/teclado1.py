import pyautogui

#clica no campo usuário
pyautogui.click(715,337, duration=0.2)
#digita a matrícula no campo
pyautogui.write('2022190002', interval=0.5)

#clica no campo senha
pyautogui.click(715,415, duration=0.2)
#digita a senha no campo
pyautogui.write('1111111111', interval=0.5)

#clica no botão acessar02
pyautogui.click(715, 476, duration=0.2)