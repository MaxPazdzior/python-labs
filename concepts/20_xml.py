# ==============================================================================

import xml.etree.ElementTree as ET

try:
    movies = ET.parse("Python/movies.xml")  # --> Hier öffnet man die XML Datei
except ET.ParseError:   # --> Parse Error, wenn etwas in der XML Datei verändert wurde und nicht richtig ist
    print("XML Kaputt!")

# print(movies)

root = movies.getroot() # --> Root: Wurzel bzw. Anfangsknoten

# ==============================================================================

# Aufgabe 1: Alle Filmtitel ausgeben
print("--- Alle Filmtitel ---")
for m in root.iter("movie"):    # --> Für jeden Film in der Movie iteration
    titel = m.find("title").text # --> Hier muss man eingeben was man suchen will zum ausgeben
    print(titel)

# ==============================================================================

# Aufgabe 2: Filme ab 2014 ausgeben
print("--- Filme ab 2014 ---")
for m in root.iter("movie"):
    jahr = int(m.find("year").text) # --> Muss man als Int angeben, weil es ein Jahr ist. Sonst wird es als String gespeichert
    if jahr >= 2014:
        titel = m.find("title").text
        print(f"{titel} ({jahr})")

# ==============================================================================

# Aufgabe 3: Durchschnittliche Bewertung ausgeben
print("--- Bewertung ---")
ratings = []

for m in root.iter("movie"):
    rating_val = float(m.find("rating").text)
    ratings.append(rating_val)

if ratings:
    avarage = sum(ratings) / len(ratings)
    print(f"{avarage:.2f}")

# ==============================================================================
