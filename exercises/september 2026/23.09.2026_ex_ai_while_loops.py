# ==============================================================================

# Das Rover-Kontrollsystem
#
# Schreibe ein Programm, das den Zugriff auf einen Mars-Rover absichert
# und anschließend ein Terminal-Menü für das Energie-Management bereitstellt.
#
# Regeln für das System:
# 1. Sicherheits-Check: Das korrekte Passwort lautet "Ares-1". Der Nutzer hat 3 Versuche.
#    Nutze eine while-Schleife und einen Zähler. Nach 3 falschen Eingaben bricht das 
#    Programm mit einer Warnung ab (System gesperrt).
#
# 2. Hauptmenü: Ist das Passwort korrekt, startet eine Endlosschleife (while True).
#    Der Rover startet mit einem Energieniveau von 40 (Prozent). Das absolute Maximum ist 100.
#
# 3. Befehle im Menü:
#    - status: Gibt die aktuelle Energie in Prozent per f-String aus.
#    - aufladen: Fragt über input nach einem Wert, wandelt ihn in eine Zahl um (int oder float) 
#      und addiert ihn zur Energie. 
#      Wichtig: Die Energie darf 100 Prozent nicht überschreiten. Wenn der neue Wert 
#      über 100 liegt, kappe ihn auf exakt 100.
#    - fahren: Fragt den Nutzer, wie viele Einheiten Energie verbraucht werden sollen.
#      Prüfe mit if, ob überhaupt genug Energie vorhanden ist. 
#      Wenn ja, ziehe den Wert ab. Wenn nein, verweigere den Befehl mit einer Fehlermeldung.
#    - standby: Verabschiedet den Nutzer und beendet das Programm (break).
#    - Bei jeder anderen Eingabe erscheint eine Fehlermeldung ("Unbekannter Befehl").

# Lösung

# versuche = 3
# programm_aktiv = True

# while programm_aktiv:

#     passwort = input("Willkommen. Bitte geben Sie nun das Passwort ein:\n")

#     if passwort == "Ares-1":
#         print("Das Passwort ist korrekt. Willkommen an Board.")
#         energie = 40

#         while True:
#             eingabe = input("Bitte gebe nun ein Befehl ein: (status, aufladen, fahren, standby)\n")

#             if eingabe == "status":
#                 print(f"Die aktuelle Energie liegt bei {energie}%.")

#             elif eingabe == "aufladen":
#                 aufladen_text = input("Wie viel Prozent sollen aufgeladen werden?\n")
#                 if aufladen_text.isnumeric():
#                     aufladen = int(aufladen_text)
#                     energie += aufladen
#                     if energie > 100:
#                         energie = 100
#                         print(f"Energie überstieg 100% und wurde gekappt. Energie beträgt nun {energie}%!")
#                     else:
#                         print(f"Ich habe mich erfolgreich aufgeladen, meine neue Energie beträgt {energie}%!")
#                 else:
#                     print("Fehler: Bitte gib eine Zahl ein.")

#             elif eingabe == "fahren":
#                 entladen_text = input("Wie viele Einheiten an Energie sollen verbraucht werden?\n")
#                 if entladen_text.isnumeric():
#                     entladen = int(entladen_text)
#                     if entladen > energie:
#                         print("So viel Energie haben wir nicht. Lade den Rover vorher auf.")
#                     else:
#                         energie -= entladen
#                         print("Alles klar ich fahre los.")
#                 else:
#                     print("Fehler: Bitte gib eine Zahl ein.")

#             elif eingabe == "standby":
#                 print(f"Ich gehe mit einem Energielevel von {energie}% nun in den Standby Mode. Auf Wiedersehen!")
#                 programm_aktiv = False
#                 break

#             else:
#                 print("Diese Eingabe kenne ich nicht. Versuche es nocheinmal!")

#     else:
#         versuche -= 1
#         if versuche > 0:
#             print(f"Du hast das falsche Passwort eingegeben. Du hast noch {versuche} Versuche!")
#         else:
#             print("Du hast 3x das falsche Passwort eingegeben. Authorisierung fehlgeschlagen!")
#             programm_aktiv = False

# ==============================================================================

# Das Frachtraum-Management
#
# Schreibe ein Programm, das den Zugang zum Frachtraum eines Raumschiffs sichert
# und ein Terminal für das Be- und Entladen bereitstellt.
#
# Regeln für das System:
# 1. Sicherheits-Check: Die korrekte Crew-ID lautet "Alpha-7". Der Nutzer hat 3 Versuche.
#    Nutze wieder eine Variable für die äußere Schleife (z. B. programm_aktiv = True) 
#    und einen Zähler für die Versuche. Nach 3 falschen Eingaben bricht das Programm ab.
#
# 2. Hauptmenü: Ist die Crew-ID korrekt, startet die Endlosschleife des Terminals.
#    Der Frachtraum startet mit einer aktuellen Ladung von 150 (Tonnen).
#
# 3. Befehle im Menü:
#    - status: Gibt die aktuelle Ladung in Tonnen per f-String aus.
#    - einladen: Fragt nach dem Gewicht, das zugeladen werden soll. 
#      Prüfe mit .isnumeric(), ob es eine Zahl ist (denke an das 'else' für Texteingaben!).
#      Wandle sie in int um und addiere sie. 
#      Wichtig: Die Maximalkapazität beträgt 500 Tonnen. Wenn der neue Wert über 500 liegt, 
#      kappe ihn auf exakt 500 und gib eine entsprechende Meldung aus.
#    - ausladen: Fragt, wie viele Tonnen entladen werden sollen.
#      Prüfe auf .isnumeric() (und das 'else'!).
#      Wichtig: Prüfe ZUERST, ob überhaupt so viel Fracht an Bord ist. 
#      Wenn die Zahl größer als die aktuelle Ladung ist, verweigere den Vorgang. 
#      Nur wenn genug da ist, ziehe den Wert ab.
#    - schliessen: Verabschiedet den Nutzer und beendet das Programm sauber 
#      (sodass beide Schleifen beendet werden!).
#    - Bei jeder anderen Eingabe erscheint die Meldung: "Unbekannter Befehl."

# Lösung

versuche = 3
programm_aktiv = True

while programm_aktiv:

    id = input("Willkommen. Bitte gib die richtige Crew-ID an um fortzufahren:\n")

    if id == "Alpha-7":
        print("Sie haben sich erfolgreich eingeloggt.")
        ladung = 150

        while True:

            eingabe = input("Bitte gib einen der folgenden Befehle ein: (status, einladen, ausladen, schliessen)\n")

            if eingabe == "status":
                print(f"Die aktuelle Ladung beträgt {ladung} Tonnen!")
            

            elif eingabe == "einladen":
                gewicht_text = input("Welches Gewicht soll zugeladen werden?\n")
                if gewicht_text.isnumeric():
                    gewicht = int(gewicht_text)
                    ladung += gewicht
                    if ladung >500:
                        ladung = 500
                        print("Die Maximale Ladungskapazität wurde überschritten. Es wurde auf 500 gekappt.")
                    else:
                        print(f"Erfolg! Das neue Gewicht beträgt: {ladung} Tonnen!")
                else:
                    print("Fehler erkannt! Gib eine Zahl ein!")

            elif eingabe == "ausladen":
                gewicht_text = input("Wie viel Gewicht soll entladen werden?\n")
                if gewicht_text.isnumeric():
                    gewicht = int(gewicht_text)
                    if gewicht > ladung:
                        print("Verweigert! So viel Ladung haben wir nicht!")
                    else:
                        ladung -= gewicht
                        print(f"Erfolg! Es wurden {gewicht} Tonnen abgezogen!")
                else:
                    print("Fehler erkannt! Gib eine Zahl ein!")

            elif eingabe == "schliessen":
                print("Das Programm wird beendet. Bis Bald!")
                programm_aktiv = False
                break

            else:
                print("Ungültige Eingabe")

    else:
        versuche -=1
        if versuche == 0:
            print("Du hast 3x das falsche Passwort eingegeben und wurdest gesperrt!")
            programm_aktiv = False
        else:
            print(f"Falsches Passwort! Du hast noch {versuche} Versuche!")