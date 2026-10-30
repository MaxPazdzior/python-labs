# ==============================================================================

# Schreibe ein Python-Programm, bei dem der Benutzer eine geheime Zahl erraten muss.

# Die Regeln:
#   1) Die geheime Zahl ist die 7.
#   2) Das Programm fragt den Benutzer in einer Schleife nach einem Tipp.
#   3) If: Wenn die getippte Zahl richtig ist, gratuliert das Programm und die Schleife endet sofort.
#   4) Else: Wenn die Zahl falsch ist, gibt das Programm einen Hinweis aus ("Falsch geraten!"), und die Schleife läuft weiter.

# Lösung:

# while True:
#     zahl = input("Errate die Geheime Zahl. Gib eine Zahl deiner Wahl ein: (0-10)\n")
#     if zahl == "7":
#         print("Herzlichen Glückwunsch! Du hast die geheime Zahl erraten")
#         break
#     else:
#         print("Falsch geraten. Mach weiter um die geheime Zahl zu finden!")


# Daniels Lösung

# geheimnis = 7
# tipp = 0

# while tipp != geheimnis:
#     tipp = int(input("Rate die Gehimzahl (zwischen 1 und 10): "))

#     if tipp == geheimnis:
#         print("Glückwunsch! Richtig erraten!")
#     else:
#         print("Falsch geraten! Versuche es noch einmal.\n")

# ==============================================================================