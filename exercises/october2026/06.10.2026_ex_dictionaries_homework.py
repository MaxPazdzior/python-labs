# ==============================================================================

# Aufgabe 1 (Grundlage)
 
# Gegeben ist ein Dictionary, das die Daten eines Laptops beschreibt:
 
laptop = {
    "marke": "Dell",
    "modell": "Inspiron 15",
    "preis": 799.00,
    "ram_gb": 16
}

print(laptop)

# # 1. Ändern Sie den Preis auf 849.99.
# # 2. Fügen Sie ein neues Schlüssel-Wert-Paar hinzu: "betriebssystem": "Windows 11".
# # 3. Geben Sie den Wert des Schlüssels "marke" auf der Konsole aus.

# # Lösung

# 1.
laptop["preis"] = 849.99
print(laptop)

# 2.
laptop["betriebssystem"] = "Windows 11"
print(laptop)

# 3.
print(laptop["marke"])

# ==============================================================================

# Aufgabe 2: Telefonbuch – Einträge filtern
 
# Sie haben ein Dictionary mit Namen und Telefonnummern.
 
telefonbuch = {
    "Anna": "030-123456",
    "Ben": "040-987654",
    "Clara": "030-555666",
    "Daniel": "089-112233"
}

print(telefonbuch)
 
# # Schreiben Sie ein Programm, das alle Personen herausfiltert und in einer Liste speichert, 
# # deren Telefonnummer mit der Vorwahl 030 (Berlin) beginnt.

# # Lösung

nummern_liste = []

for name, nummer in telefonbuch.items():
    if nummer.startswith("030"):
        nummern_liste.append([name,nummer])
print(f" Folgende Personen, haben die Vorwahl: 030: {nummern_liste}")

# ==============================================================================

# Aufgabe 3: Häufigkeitszähler
 
# Gegeben ist ein Text als String.
# text = "Python ist super"
# Schreiben Sie ein Programm, das ein Dictionary erstellt und ausgibt, das zählt, wie oft jeder Buchstabe in dem Text vorkommt.
# Ignorieren Sie dabei die Groß-/Kleinschreibung sowie Leerzeichen.

# Lösung

text = "Python ist super".lower()
text_dict = {}

for buchstabe in text:
    if buchstabe == " ":
        continue
    if buchstabe not in text_dict:
        text_dict[buchstabe] = 1
    else:
        text_dict[buchstabe] += 1

print(text_dict)

# ==============================================================================

# Aufgabe 04: Gebirgsdaten
 
# Gegeben ist eine Datenbank mit bekannten Bergen, deren Hoehe in Metern und dem jeweiligen Kontinent, auf dem sie liegen.
# Schreiben Sie ein Programm, das:
# 1. Den höchsten Berg ermittelt und namentlich mit seiner Hoehe ausgibt.
# 2. Die durchschnittliche Hoehe aller Berge berechnet (gerundet auf zwei Nachkommastellen) und ausgibt.
 
berge_daten = {
    "Mount Everest": {"Hoehe": 8848, "Kontinent": "Asien"},
    "Mont Blanc": {"Hoehe": 4810, "Kontinent": "Europa"},
    "Kilimandscharo": {"Hoehe": 5895, "Kontinent": "Afrika"},
    "Denali": {"Hoehe": 6190, "Kontinent": "Nordamerika"},
    "Aconcagua": {"Hoehe": 6961, "Kontinent": "Südamerika"}
}

# Lösung

#Aufgabe 2.
berg_daten = []

for namen, daten in berge_daten.items():
    berg_daten.append(daten["Hoehe"])
    schnitt = sum(berg_daten) / len(berg_daten)


print(f"Der Durchschnitt aller Berge beträgt: {schnitt:.2f}")

# Aufgabe 1
höhe = max(berg_daten)
    
for namen, daten in berge_daten.items():
    if daten["Hoehe"] == höhe:
        break
print(f"Der {namen} ist der Höhste Berg mit ca. {höhe} Metern.")

# ==============================================================================
