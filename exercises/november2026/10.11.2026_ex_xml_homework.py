# ==============================================================================

import xml.etree.ElementTree as ET

try:
    movies = ET.parse("Aufgaben/November 2026/movies.xml")
except ET.ParseError:
    print("XML Kaputt!")

root = movies.getroot()

# ==============================================================================

# Aufgabe 1: Alle Filme von Christopher Nolan ausgeben

# Lösung

print("--- Filme von Christopher Nolan ---")
for m in root.iter("movie"):
    titel = m.find("title").text
    directors = m.find("director").text
    if directors == "Christopher Nolan":
        print(titel)

# ==============================================================================

# Aufgabe 2: Alle Filme länger als 150 Minuten ausgeben

# Lösung

print("--- Filme die Länger sind als 150 Minuten ---")
for m in root.iter("movie"):
    titel = m.find("title").text
    laenge = int(m.find("runtime_min").text)
    if laenge >150:
        print(titel)

# ==============================================================================

# Aufgabe 3: Regisseure ohne Duplikate auflisten

# Lösung

regi = set()

print("--- Alle Regisseure ---")
for m in root.iter("movie"):
    directors = m.find("director").text
    regi.add(directors)

for r in regi:
    print(r)

# ==============================================================================

# Aufgabe 4: Filmtitel nach Anfangsbuchstaben filtern

# Lösung

while True:
    user_input = input("\nGib einen Buchstabe ein, oder gib 'Ende' ein um das Programm zu beenden.\n").strip().capitalize()

    if user_input == "Ende":
        print("Auf wiedersehen!")
        break

    gefunden = False

    for m in root.iter("movie"):
        titel = m.find("title").text
        if titel.startswith(user_input):
            gefunden = True
            print(f"Titel gefunden: {titel}")
        
    if not gefunden:
        print(f"Ein Titel mit dem Buchstaben {user_input} existiert nicht.")

# ==============================================================================

# Aufgabe 5: Anzahl der Animationsfilme ausgeben

# Lösung

anzahl = 0

for m in root.iter("movie"):
    kategorie = m.find("category").text
    if kategorie == "Animation":
        anzahl +=1

print(f"Es wurden {anzahl} Filme mit der Kategorie 'Animation' gefunden!")

# ==============================================================================
