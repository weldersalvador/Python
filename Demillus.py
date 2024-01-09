import webbrowser
import pyautogui
from time import sleep
#abrir o opera
pyautogui.alert('APERTE EM "OK" E NÃO FAÇA NADA')
pyautogui.press('winleft')
pyautogui.write('opera')
sleep(1)
pyautogui.press('enter')
sleep(2)
#entrar no site da demillus
pyautogui.write('https://www.demillus.com.br/portalpedidos/Web')
sleep(1)
pyautogui.press('enter')
#logar e deixar no pedido
sleep(2)
pyautogui.moveTo(x=983, y=657)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=1349, y=563)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=1091, y=446)
pyautogui.click()
pyautogui.alert('PROGRAMA FINALIZADO. APERTE EM "OK" PARA CONTINUAR')