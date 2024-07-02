import pyautogui

#clica no chrome
pyautogui.click(200, 325, duration=.5)
pyautogui.keyDown('space')

#pressionar espaço                                   
while True: 
    #print(pyautogui.pixel(200, 422))             
    if not pyautogui.pixelMatchesColor(200, 325, [255,255,255], tolerance=.1):
        pyautogui.keyDown('space')