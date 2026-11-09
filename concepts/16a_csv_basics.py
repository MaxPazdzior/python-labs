# ==============================================================================

import csv
liste_csv = []

try:
    with open("Python/Kundeninfos.csv", mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            liste_csv.append(row)
except FileNotFoundError:
    print("Error: File not found.")

print(liste_csv)

# ==============================================================================

dict_csv= []

try:
    with open ("Python/Kundeninfos.csv", mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            dict_csv.append(row)
except FileNotFoundError:
    print("Error: File not found")

print(dict_csv)

# ==============================================================================
# ERKLÄRUNGEN ZU CODE 1: csv.reader()
# ==============================================================================
#
# import csv
#     Importiert das csv-Modul, um CSV-Dateien zu lesen und zu verarbeiten.
#
# liste_csv = []
#     Erstellt eine leere Liste, in der später alle CSV-Zeilen gespeichert werden.
#
# mode="r"
#     Öffnet die Datei im Lesemodus (read). Die Datei wird nur gelesen.
#
# encoding="UTF-8"
#     Legt die Zeichenkodierung fest, damit Zeichen wie ä, ö und ü
#     korrekt gelesen werden können, wenn die Datei UTF-8 verwendet.
#
# newline=""
#     Überlässt dem csv-Modul die Verarbeitung von Zeilenumbrüchen,
#     um Probleme mit zusätzlichen Leerzeilen zu vermeiden.
#
# with open(...)
#     Öffnet die Datei und schließt sie automatisch, sobald der Block endet.
#
# as file
#     Speichert das geöffnete Dateiobjekt unter dem Namen "file".
#
# delimiter=";"
#     Legt fest, dass ein Semikolon die einzelnen Spalten trennt.
#     Beispiel: "Max;Müller;25" wird in drei Werte aufgeteilt.
#
# csv.reader(file, delimiter=";")
#     Liest jede CSV-Zeile als Liste.
#     Einzelne Werte werden über ihre Position angesprochen, z. B. row[0].
#
# for row in reader
#     Durchläuft jede Zeile, die der CSV-Leser zurückgibt.
#
# append(row)
#     Fügt die aktuelle Zeile am Ende der Liste hinzu.
#
# try:
#     Startet einen Block, in dem mögliche Fehler abgefangen werden können.
#
# except FileNotFoundError:
#     Fängt den Fehler ab, wenn die Datei nicht gefunden wird.
#
# print(liste_csv)
#     Gibt die gesamte Liste mit den eingelesenen Zeilen aus.
#
# ==============================================================================
# ERKLÄRUNGEN ZU CODE 2: csv.DictReader()
# ==============================================================================
#
# dict_csv = []
#     Erstellt eine leere Liste, in der alle Datensätze gespeichert werden.
#
# mode="r"
#     Öffnet die Datei im Lesemodus (read).
#
# encoding="UTF-8"
#     Legt fest, wie Zeichen aus der Datei dekodiert werden.
#
# newline=""
#     Überlässt dem csv-Modul die Verarbeitung der Zeilenumbrüche.
#
# with open(...)
#     Öffnet die Datei und schließt sie nach der Verarbeitung automatisch.
#
# as file
#     Speichert das geöffnete Dateiobjekt unter dem Namen "file".
#
# delimiter=";"
#     Bestimmt das Trennzeichen zwischen den Spalten.
#     Beispiel: "Vorname;Nachname;Alter" enthält drei Spalten.
#
# csv.DictReader(file, delimiter=";")
#     Liest die erste Zeile als Spaltenüberschriften.
#     Diese Überschriften werden zu Schlüsseln der Dictionaries.
#     Beispiel: row["Vorname"] liefert den Wert aus der Spalte "Vorname".
#
# for row in reader
#     Durchläuft jeden Datensatz der CSV-Datei.
#     Jeder Datensatz wird als Dictionary zurückgegeben.
#
# append(row)
#     Fügt das Dictionary zur Liste hinzu.
#
# try:
#     Ermöglicht es, mögliche Fehler im Code abzufangen.
#
# except FileNotFoundError:
#     Wird ausgeführt, wenn die Datei nicht gefunden wird.
#
# print(dict_csv)
#     Gibt die Liste mit allen eingelesenen Dictionaries aus.
#
# ==============================================================================
# WICHTIGSTER UNTERSCHIED
# ==============================================================================
#
# csv.reader()
#     Speichert jede Zeile als Liste.
#     Zugriff über Positionen, z. B. row[0].
#
# csv.DictReader()
#     Speichert jede Zeile als Dictionary.
#     Zugriff über Spaltennamen, z. B. row["Vorname"].
#
# DictReader ist besonders praktisch, wenn man Werte anhand ihrer
# Spaltenüberschriften statt anhand ihrer Position abrufen möchte.
#
# ==============================================================================
