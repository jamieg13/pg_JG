
import pyautogui as pg
import webbrowser
import time

Book = pg.prompt(
    """
What book did you forget?
a)To Kill a Mockingbird
b)Black Like Me
c)Of Mice and Men

""")

if Book == "a":
    category = pg.prompt(
        """
What part is it?
a)Part One
b)Part Two

        """)

elif Book == "b":
    category = pg.prompt(
        """
What part is it?
a)part 1
b)part 2
c)part 3

""")

elif Book =="c":
    category = pg.prompt(
        """
What chapter is it?
a)Chapter 1
b)Chapter 3
c)Chapter 6
    
pg.alert("""
If you are in immediate danger, please call 911 immediately.
Follow the instructions in the webpages that open following this message for other guidance.
""")
if emergency == "a":
    if category == "a":
        webbrowser.open("http://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts")
    elif category == "b":
        webbrowser.open("https://www.ready.gov/floods")

elif emergency == "b":
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=PA9hpOnvtCk")
    elif category == "b":
        webbrowser.open("https://www.mayoclinic.org/first-aid/first-aid-heart-attack/basics/art-20056679")
