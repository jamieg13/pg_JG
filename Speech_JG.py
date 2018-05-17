import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name?")
answer = pg.prompt("Enter your name.")

if answer == "Jamie":
    speak.Speak ("Hello" + answer + "nice to meet you.")

elif answer == "Vaughn":
    speak.Speak("I am your Daddy")

else:
    speak.Speak("Nice to meet you," + answer)

speak.Speak("What is your favorite game?")
game = pg.prompt("Enter favorite game.")

if game == "Fortnite":
    speak.Speak("Stop watching Fortnite videos during school!")
else:
    speak.Speak ("I also like to play" + game + "." + "Let's watch a video about" + game + "on Youtube")
    wb.open("https://www.youtube.com/results?search_query="+game)
