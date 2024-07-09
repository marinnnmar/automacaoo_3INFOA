import pyautogui

while True:
    try:
        ponto = pyautogui.locateOnScreen('bolinhaa.png', grayscale=True, region=[0,89,846,591], confidence=0.5)

        pyautogui.click(ponto, duration=0.1)
    except:
        print("Não encontrada bolinha")