import pyautogui


#localizar x, y de uma imagem na tela
nome_XY = pyautogui.locateCenterOnScreen('./semana7/campo_nome.png')
pyautogui.click(nome_XY, duration=0.5) #clica
pyautogui.write('Mariana Marcilio de Carvalho')

cpf_XY = pyautogui.locateCenterOnScreen('./semana7/campo_cpf.png')
pyautogui.click(cpf_XY, duration=0.5) #clica
pyautogui.write('123.456.789-10')

sim_XY = pyautogui.locateCenterOnScreen('./semana7/sim.png')
pyautogui.click(sim_XY, duration=0.5) #clica

registrar_XY = pyautogui.locateCenterOnScreen('./semana7/registrar.png')
pyautogui.click(registrar_XY, duration=0.5) #clica