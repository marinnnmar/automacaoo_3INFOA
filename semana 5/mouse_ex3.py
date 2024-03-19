import pyautogui

pyautogui.moveTo(300, 300, duration=0.2)

distancia = 400
while distancia > 0:
    pyautogui.dragRel(distancia, 0, duration=0.2)
    distancia = distancia - 10
    pyautogui.dragRel(0, distancia, duration=0.2)
    pyautogui.dragRel(-distancia, 0, duration=0.2)
    distancia = distancia - 10
    pyautogui.dragRel(0, -distancia, duration=0.2)

