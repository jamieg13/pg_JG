import webbrowser
name = "Jamie"

subjects = ["English","Spanish","History","Math","Science"]

print("Hello"+ name)

print(subjects)

for i in subjects:
    print("One of my classes  is" + i)
videogames = ["Fortnite", "COD", "Destiny 2", "Halo", "Star Wars Battlefront"]

for i in videogames:
    if i == "Fortnite":
        print(i + "is a hard game.")
    elif i == "COD":
        print(i + "is a bad game right now.")
    elif i == "Destiny 2":
        print(i + "is a grind.")
    else:
        print("One of the best games is " + i)

movies = []

while True:
    print("What is a movie you like? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorites is" + i)
    webbrowser.open(i)
    
