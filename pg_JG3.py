import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.2)
pg.hotkey('winleft','up')
pg.typewrite('youtube.com\n',0.2)
time.sleep(3)
