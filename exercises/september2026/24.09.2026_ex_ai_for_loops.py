# ==============================================================================

# AUFGABE 1: Der Zahlen-Filter
# Ziel: Lösche alle Zahlen (0-9). Buchstaben bleiben normal.
# Tipp: Wenn eine Zahl kommt, fügst du einfach gar nichts hinzu.

# Lösung

# text = "Geheimcode2026"
# neuer_text = ""

# for i in text:
#     if i in "0123456789":
#         neuer_text += ""
#     else:
#         neuer_text += i
# print(neuer_text)

# ==============================================================================

# AUFGABE 2: Der Doppel-Ersetzer
# Ziel: Ersetze "X/x" durch "A" UND "Z/z" durch "B". Rest bleibt normal.
# Tipp: Nutze "if" für X, "elif" für Z und "else" für den Rest.

# Lösung

# text = "Xylophon und Zebra"
# neuer_text = ""

# for i in text:
#     if i in "Xx":
#         neuer_text += "A"
#     elif i in "Zz":
#         neuer_text += "B"
#     else:
#         neuer_text += i
# print(neuer_text)

# =====================================================================

# AUFGABE 3: Der Großbuchstaben-Zähler
# Ziel: Zähle, wie viele Großbuchstaben im Wort stecken.
# Tipp: Starte bei 0 und rechne bei jedem Treffer "+= 1".


# text = "PythonProgramm"
# zahl = 0

# for i in text:
#     if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         zahl += 1
# print(f"Es sind {zahl} Großbuchstaben im Text!")

# =====================================================================

# AUFGABE 4: Der Vokal-Dreher
# Ziel: Ersetze jedes "A" durch "O", jedes "a" durch "o", jedes "O" 
# durch "A" und jedes "o" durch "a". Alle anderen Zeichen bleiben normal.

# text = "Oma fährt Auto"
# neuer_text = ""

# for i in text:
#     if i in "A":
#         neuer_text += "O"
#     elif i in "a":
#         neuer_text += "o"
#     elif i in "O":
#         neuer_text += "A"
#     elif i in "o":
#         neuer_text += "a"
#     else:
#         neuer_text += i
# print(neuer_text)


# =====================================================================
# AUFGABE 5: Der Zensor
# Ziel: Wenn ein Buchstabe direkt doppelt hintereinander vorkommt, 
# soll der zweite Buchstabe durch ein "X" ersetzt werden.

# text = "Hallo"
# neuer_text = ""
# letzer_buchstabe = ""

# for i in text:
#     if i == letzer_buchstabe:
#         neuer_text += "X"
#     else: neuer_text += i
#     letzer_buchstabe = i
# print(neuer_text)

# =====================================================================
# AUFGABE 6: Der Wort-Zähler
# Ziel: Zähle, wie viele Wörter in dem Satz stecken.

# text = "Ich lerne gerade Python Programmieren"
# wort = 1

# for i in text:
#     if i in " ":
#         wort += 1
# print(f"Es sind {wort} Wörter im Satz")

# =====================================================================

# Hausaufgabe 03: Roboter im Tunnel
#
# Schreibe ein Steuerungsprogramm für einen Roboter, der sich in einem Tunnel bewegt.
# Der Roboter startet immer bei Position 0 (der Basis).
#
# Die Befehle im Eingabetext:
# - 'R' = 1 Schritt nach Rechts (Position +1)
# - 'L' = 1 Schritt nach Links (Position -1)
# - Alle anderen Zeichen (z. B. Leerzeichen oder andere Buchstaben) werden ignoriert.
#
# Die Regeln:
# 1. Wand-Schutz: Der Roboter darf sich NIEMALS links von seiner Basis bewegen (Position < 0).
#    Sobald das passiert, stoppt die Analyse sofort -> Ausgabe: "Absturz: Gegen die Wand gefahren!"
# 2. Ziel: Am Ende der Befehlskette muss der Roboter wieder EXAKT auf Position 0 stehen.
#    Steht er woanders -> Ausgabe: "Ungültig: Roboter steht nicht an der Basis!"
# 3. Wenn alle Regeln eingehalten wurden -> Ausgabe: "Route erfolgreich beendet!"
#
# Beispiele zum Testen:
# "R R L L" -> Route erfolgreich beendet!
# "L R R"   -> Absturz: Gegen die Wand gefahren!
# "R R L"   -> Ungültig: Roboter steht nicht an der Basis!

# Lösung

# while True:
#     eingabe = input("Gib ein, wohin der Roboter fahren soll (L,R) oder gib exit ein um zu beenden\n")

#     if eingabe == "exit":
#         print("Bis Bald!")
#         break

#     position = 0
#     gültig = True

#     for i in eingabe:
#         if i == "R":
#             position +=1
#         elif i == "L":
#             position -=1

#         if position < 0:
#             print("Absturz gegen die Wand gefahren!")
#             gültig = False
#             break

#     if gültig and position !=0:
#         print("Ungültig: Roboter steht nicht an der Basis!")
#         gültig = False

#     if gültig:
#         print("Route erfolgreich beendet!")

# =====================================================================

# Hausaufgabe 04: Der Fahrstuhl im Hochhaus

# Schreibe ein Steuerungsprogramm für einen Fahrstuhl.
# Der Fahrstuhl startet immer im Erdgeschoss (Etage 0).
# Das Gebäude hat Etagen von 0 (Erdgeschoss) bis 5 (Dachgeschoss).

# Die Befehle im Eingabetext:
# - 'U' = Up / Hoch (Etage +1)
# - 'D' = Down / Runter (Etage -1)
# - Alle anderen Zeichen werden ignoriert.

# Die Regeln:
# 1. Untere Grenze: Der Fahrstuhl darf NIEMALS unter Etage 0 fahren (Etage < 0).
#    -> Sofort abbrechen mit Ausgabe: "Fehler: Der Fahrstuhl kann nicht in den Boden fahren!"
# 2. Obere Grenze: Der Fahrstuhl darf NIEMALS über Etage 5 fahren (Etage > 5).
#    -> Sofort abbrechen mit Ausgabe: "Fehler: Der Fahrstuhl ist durchs Dach geschossen!"
# 3. Ziel: Am Ende muss der Fahrstuhl wieder EXAKT im Erdgeschoss (Etage 0) stehen.
#    Steht er woanders -> Ausgabe: "Ungültig: Der Fahrstuhl steht nicht im Erdgeschoss!"
# 4. Wenn alle Regeln eingehalten wurden -> Ausgabe: "Fahrstuhl-Fahrt erfolgreich!"

# Beispiele zum Testen:
# "U U D D"   -> Fahrstuhl-Fahrt erfolgreich!
# "D U U"     -> Fehler: Der Fahrstuhl kann nicht in den Boden fahren!
# "U U U U U U" -> Fehler: Der Fahrstuhl ist durchs Dach geschossen!
# "U U D"     -> Ungültig: Der Fahrstuhl steht nicht im Erdgeschoss!

# Lösung

# while True:
#     eingabe = input("Gib ein in welches Stockwerk du fahren möchtest (U,D) oder drücke exit wenn du den Fahrstuhl verlassen willst!\n")

#     if eingabe == "exit":
#         print("Auf Wiedersehen!")
#         break

#     position = 0
#     gültig = True

#     for i in eingabe:
#         if i == "U":
#             position += 1
#         elif i == "D":
#             position -= 1

#         if position <0:
#             print("Fehler! Der Fahrstuhl kann nicht in den Boden fahren!")
#             gültig = False
#             break
#         elif position >5:
#             print("Fehler: Der Fahrstuhl ist durchs Dach geschossen!")
#             gültig = False
#             break

#     if position !=0 and gültig:
#         print("Ungültig! Der Fahrstuhl steht nicht im Erdgeschoss!")
#         gültig = False

#     if gültig:
#         print("Fahrstuhl Fahrt erfolgreich!")

# =====================================================================