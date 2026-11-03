# ==============================================================================

import random

# ==============================================================================

# Beispiel 01: Name Generator

vorsilben = ["Ar", "Bra", "Gral", "Tho"]
mittelsilben = ["da", "do", "rin", "ma"]
nachsilben = ["kus", "nus", "rion", "li"]

name = random.choice(vorsilben) + random.choice(mittelsilben) + random.choice(nachsilben)
print(f"Dein neuer Charakter heißt: {name}")

# ==============================================================================

# Beispiel 02: Speisekarte (Dict), ein Gericht wählen, was "günstig" ist

speisekarte = {
    "Pizza":"günstig",
    "Sushi":"teuer",
    "Döner":"günstig",
    "Burger":"mittel",
    "Tapioca":"teuer",
    "Steak":"teuer"
}

auswahl = []
for gericht, preis in speisekarte.items():
    if preis == "günstig":
        auswahl.append(gericht)
print(f"Die günstigen Gerichte auf unserer Speisekarte sind: {auswahl}")
print(f"Heute gibt es: {random.choice(auswahl)}")

# ==============================================================================

# Beispiel 03: Rabatt-Würfler

rabatte = [5,10,20,50]
wahrscheinlichkeiten = [0.50, 0.35, 0.13, 0.02]

gewinn = random.choices(rabatte, weights=wahrscheinlichkeiten, k=1)
print(f"Du erhälst {gewinn[0]}% Rabatt!")       # --> Die 0 steht hier, damit die Ausgabe nicht als Liste angezeigt wird, damit nur die 0 Stelle gezeigt wird

# ==============================================================================

# Beispiel 04: Zufällige Farbe generieren

def draw_monkey():
    text = "@('_')@"

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)


    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")        # --> 033 ist für das Terminal

draw_monkey()

# ==============================================================================
