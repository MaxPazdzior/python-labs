# ==============================================================================
# Aufgabe 3) Der Firmen-Jubiläums-Rechner
#
# Ein Unternehmen zahlt seinen Mitarbeitern je nach Anzahl ihrer Dienstjahre
# eine Treueprämie.
#
# Schreibe ein Programm, das den Benutzer nach den Dienstjahren eines 
# Mitarbeiters fragt (int()).
#
# Prüfe mit einer if-elif-else-Struktur und dem Modulo-Operator (%),
# welcher Bonus dem Mitarbeiter zusteht:
#   - Jedes 25. Dienstjahr (z. B. 25, 50, 75): "Gold-Bonus (500 €)"
#   - Jedes 10. Dienstjahr (z. B. 10, 20, 30, 40): "Silber-Bonus (250 €)"
#   - Jedes 5. Dienstjahr (z. B. 5, 15, 35): "Bronze-Bonus (100 €)"
#   - Alle anderen Jahre: "Kein Bonus"
#
# WICHTIG: Achte auf die richtige Reihenfolge der Bedingungen!
#
# Testwerte für dein Programm:
# - 50 -> Gold-Bonus (500 €)   [Teilbar durch 25, 10 und 5 -> 25 hat Vorrang!]
# - 20 -> Silber-Bonus (250 €) [Teilbar durch 10 und 5 -> 10 hat Vorrang!]
# - 15 -> Bronze-Bonus (100 €)
# - 7  -> Kein Bonus

# Lösung

# input("Willkommen bei deinem Firmen-Juniläums-Rechner! Drücke Enter zum starten\n")

# dienstjahr = int(input("Bitte gib an, Wie viele Dienstjahre du schon im Unternehmen arbeitest.\n"))

# if dienstjahr % 25 == 0:
#     print("\nDa du bereits seit",dienstjahr,"Dienstjahren bei uns arbeitest, erhälst du den Goldbonus.\n500€ werden dir gutgeschrieben.")
# elif dienstjahr % 10 == 0:
#     print("\nDa du bereits seit",dienstjahr,"Dienstjahren bei uns arbeitest, erhälst du den Silberbonus.\n250€ werden dir gutgeschrieben.")
# elif dienstjahr % 5 == 0:
#     print("\nDa du bereits seit",dienstjahr,"Dienstjahren bei uns arbeitest, erhälst du den Bronzebonus.\n100€ werden dir gutgeschrieben.")
# else:
#     print("\nLeider bekommst du keinen Bonus von uns. Häng dich weiter rein!")

# input("\nFertig! Drücke Enter zum beenden!")

# ==============================================================================