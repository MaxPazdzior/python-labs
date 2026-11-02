# ==============================================================================

# Aufgabe: Analyse historischer Erdbebendaten

# Themen: CSV-Datei, Dictionary, Funktionen, Tupel, f-Strings, Try-Except
# Entwickeln Sie ein Python-Programm, das globale Erdbebendaten aus einer CSV-Datei einliest, das stärkste Erdbeben ermittelt und das Land mit den häufigsten Beben identifiziert.

# Anforderungen:
# Dateiverarbeitung & Fehlerbehandlung:
# • Lesen Sie eine CSV-Datei namens erdbeben.csv mithilfe des csv.reader-Moduls ein.
# • Überspringen Sie die Kopfzeile (Header) der Datei vor der Verarbeitung.
# • Sichern Sie das Programm gegen einen FileNotFoundError ab und geben Sie im Fehlerfall eine passende Meldung aus.

# Auswertung des stärksten Erdbebens:
# • Iterieren Sie durch die Datenzeilen (Spalten: Jahr, Land, Region, Magnitude).
# • Ermitteln Sie das Beben mit der höchsten Magnitude.
# • Speichern Sie die Details dieses Bebens (Jahr, Land, Region und Stärke) dynamisch in einem Dictionary ab.

# Häufigkeitsanalyse per Hilfsfunktion:
# • Zählen Sie mithilfe eines Dictionaries (land_zaehler), wie oft jedes Land in der Liste auftaucht.
# • Schreiben Sie eine separate Funktion finde_max_land(laender_daten), die dieses Dictionary auswertet. 
#       Die Funktion soll das Land mit den meisten registrierten Beben sowie die genaue Anzahl als Tupel zurückgeben.

# Ergebnisausgabe:
# • Geben Sie die Details des stärksten Erdbebens formatiert auf der Konsole aus.
# • Geben Sie direkt darunter aus, welches Land am häufigsten betroffen war und wie viele Beben dort gezählt wurden.

# ==============================================================================

import csv

csv_path = "Aufgaben/November 2026/erdbeben.csv"
erdbeben_liste = []

try:
    with open(csv_path, mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file,delimiter=",")
        next (reader)
        for row in reader:
            erdbeben_liste.append(row)
except FileNotFoundError:
    print("Die angegebene Datei wurde nicht gefunden")

staerkstes_beben = {
    "Jahr": None,
    "Land": None,
    "Region": None,
    "Magnitude": 0.0
}

for jahr, land, region, magnitude in erdbeben_liste:
    magnitude = float(magnitude)
    if magnitude > staerkstes_beben ["Magnitude"]:
        staerkstes_beben ["Jahr"] = jahr
        staerkstes_beben ["Land"] = land
        staerkstes_beben ["Region"] = region
        staerkstes_beben ["Magnitude"] = magnitude
print(f"Das stärkste Erdbeben wurde ermittelt:\n{staerkstes_beben}")


land_zaehler= {}

for jahr, land, region, magnitude in erdbeben_liste:
    if land not in land_zaehler:
        land_zaehler [land] = 1
    else:
        land_zaehler [land] +=1
print(f"Hier die Länder, in denen Erdbeben gemessen wurden und wie oft dies passiert ist:\n{land_zaehler}")


def finde_max_land(laender_daten):
    bestes_land = ""
    hoechste_anzahl = 0
    for land, anzahl in laender_daten.items():
        if anzahl > hoechste_anzahl:
            bestes_land = land
            hoechste_anzahl = anzahl
    return bestes_land, hoechste_anzahl

bestes_land, hoechste_anzahl = finde_max_land(land_zaehler)
print(f"Das Land mit den meisten Erdbeben ist: {bestes_land} mit einer Anzahl von {hoechste_anzahl} Erdbeben.")

# ==============================================================================
