import pyautogui as pg
import time
import webbrowser

points = 0

# Question

answer = pg.prompt(
"""
Which do you like more?

a)Custromization
b)Battle Royal
c)Multiplayer
"""
    )


# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


    # Question

answer = pg.prompt(
"""
Where do you end up?

a)100% completion
b)Victory Royale
c)Victory
"""
    )


# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
 # Question

answer = pg.prompt(
"""
How much XP do you earn?

a)Level Up
b)600
c)100
"""
    )


# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question

answer = pg.prompt(
"""
What do you earn?

a)Weapons and Armor
b)Skins and Pickaxes
c)Closer to ending Challenges
"""
    )


# Give points

if answer == "a":
    points +=1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# End of Survey

pg.alert("You are...")

# Destiny 2
if points < 5:
    pg.alert("Destiny 2")
    webbrowser.open("http://gamesandjunk.net/wp-content/uploads/2017/09/F83YpiMXCUkeyE6JQ4TXki.jpg")
    

# Fortnite
elif points >=5 and points < 8:
    pg.alert("Fortnite")
    webbrowser.open("https://cdn2.unrealengine.com/Fortnite%2Fhome%2Ffn_battle_royale-1268x717-cf9fa8a783c249aa8d6929126e29f5f190620357.jpg")

# COD
elif points >9:
    pg.alert("Call of Duty")
    webbrowser.open("https://cdn.images.express.co.uk/img/dynamic/galleries/x701/238137.jpg")
