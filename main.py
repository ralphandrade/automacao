# importação da biblioteca
import pyautogui as auto
import time

# define espera para cada comando auto
auto.PAUSE = 0.5

# abre o menu iniciar
auto.press('win')
# abre o chrome
auto.write('chrome')
auto.press('enter')
#abre o github
auto.write('github.com')
auto.press('enter')
#abre o classroom
time.sleep(3)
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')


