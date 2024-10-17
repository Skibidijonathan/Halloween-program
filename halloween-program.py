# halloween.py

# Fråga användaren om deras favorit-Halloween-karaktär
karaktar = input("Vilken är din favorit-Halloween-karaktär? (vampyr, zombie, spöke, varulv, vatten, mango): ").lower()

# Använd en if-sats för att ge ett svar baserat på användarens val
if karaktar == "vampyr":
    print("Blod är livet!")
elif karaktar == "zombie":
    print("Hjärnor... hjärnor...")
elif karaktar == "spöke":
    print("Buuuu!")
elif karaktar == "varulv":
    print("Du är sigma lone wolf")
elif karaktar == "vatten":
    print("dop dop")
elif karaktar == "mango":
    print("Mango fein Mango fein Mango fein Mango fein Mango fein Mango fein Mango fein Mango fein")
else:
    print("Det låter som en spännande karaktär!")
