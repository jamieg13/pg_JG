import pyautogui as pg

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.3)
pg.typewrite('youtube.com\n',0.3)
time.sleep(4)
pg.moveto('703, 635')
pg.click()
