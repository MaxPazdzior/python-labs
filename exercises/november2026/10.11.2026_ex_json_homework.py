# ==============================================================================

import json

with open("Aufgaben/November 2026/firma.json", "r", encoding="utf-8") as file:
    daten = json.load(file)

# ==============================================================================

# Aufgabe 1: Python-Spzialisten finden

# Lösung

print("--- Python Spezialisten ---")
for abteilung in daten["abteilungen"]:
    for mitarbeiter in abteilung["mitarbeiter"]:
        spezi = mitarbeiter["skills"]

        if "Python" in spezi:
            print(f"{mitarbeiter["name"]}")


# ==============================================================================

# Aufgabe 2: Gehalt im Marketing erhöhen (+10%)

# Lösung
for abteilung in daten ["abteilungen"]:
    if abteilung["name"] == "Marketing":
        for arbeiter in abteilung["mitarbeiter"]:
                arbeiter["gehalt"] = arbeiter["gehalt"] * 1.1
                print(f"{arbeiter["gehalt"]:.2f}")

# ==============================================================================
