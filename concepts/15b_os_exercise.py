# ==============================================================================


import os       # Ermöglicht den Zugriff auf Dateien und Ordner

def finde_datei_infos(ordner_pfad):         # Sucht die größte und älteste Datei im Ordner
    groesste_datei = ""         # Speichert den Namen der bisher größten Datei
    aelteste_datei = ""         # Speichert den Namen der bisher ältesten Datei
    max_groesse = -1        # Startwert, damit die erste Datei als größte erkannt wird
    min_zeit = float("inf")         # Unendlich als Startwert für den ältesten Zeitstempel

    for eintrag in os.scandir(ordner_pfad):         # Durchläuft alle Einträge im angegebenen Ordner
        if eintrag.is_file():       # Prüft, ob der Eintrag eine Datei ist
            infos = eintrag.stat()          # Liest Metadaten wie Dateigröße und Zeitstempel aus

            if infos.st_size > max_groesse:         # Prüft, ob die Datei größer als die bisherige ist
                max_groesse = infos.st_size         # Aktualisiert die bisher größte Dateigröße
                groesste_datei = eintrag.name       # Speichert den Namen der größten Datei

            if infos.st_birthtime < min_zeit:       # Prüft, ob die Datei älter als die bisherige ist
                min_zeit = infos.st_birthtime       # Aktualisiert den ältesten Zeitstempel
                aelteste_datei = eintrag.name       # Speichert den Namen der ältesten Datei

    return groesste_datei, aelteste_datei       # Gibt beide Dateinamen als Tupel zurück

pfad = "Python"         # Legt den zu untersuchenden Ordner fest
groesse, alter = finde_datei_infos(pfad)        # Speichert die beiden Rückgabewerte in Variablen
print(f"Größte Datei: {groesse}\nÄlteste Datei: {alter}")       # Gibt beide Dateinamen aus

# ==============================================================================