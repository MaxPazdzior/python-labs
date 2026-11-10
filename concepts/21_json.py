# ==============================================================================

import json

with open("Python/firma.json","r",encoding="utf-8") as datei:
    daten = json.load(datei)

# ==============================================================================

# Aufgabe 1: Gesamtgehalt berechnen
gesamtgehalt = 0

for abteilung in daten["abteilungen"]:
    for mitarbeiter in abteilung["mitarbeiter"]:
        gesamtgehalt += mitarbeiter["gehalt"]

print(f"Das Gesamtgehalt beträgt: {gesamtgehalt}€")

# ==============================================================================

with open("firma_aktualisiert.json", "w", encoding="utf-8") as ziel:    # --> "w" heißt schreibmodus
    json.dump(daten, ziel, ensure_ascii=False, indent=4)   # --> Speichert ein Dict in eine Datei / ensure_ascii muss auf false stehen sonst wird unser utf-8 zu ascii / indent = abstand. 4 Bedeutet 4 Leerzeichen 

# ==============================================================================
