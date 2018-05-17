import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=EsgVwrC-G5w","https://www.youtube.com/watch?v=jwerp2SNiTQ"]

music = ["https://www.spotify.com/us/", "https://soundcloud.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch Videos
b) Listen to Music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
