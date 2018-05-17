import pyautogui as pg
import time

points = 0

# Question

answer = pg.prompt(
"""
Which do you like more?

a)custromization
b)battle royal
c)quests
"""
    )


# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
