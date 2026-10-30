# ==============================================================================

# Aufgabe 1) Der BMI-Rechner mit Gewichtsklasse
 
# Schreibe ein Programm zur Berechnung des Body-Mass-Index (BMI). 
# Frage den Benutzer nach seinem Gewicht in Kilogramm (z. B. 75.5) und seiner Körpergröße in Metern (z. B. 1.75).

# Nutze für beide float().
# Berechne den BMI mit der Formel: BMI = Gewicht/(Größe**2)

# Nutze eine if-elif-else-Struktur, um dem Benutzer seine Gewichtsklasse auszugeben:

        # - BMI unter 18.5: "Untergewicht"
        # - BMI von 18.5 bis unter 25: "Normalgewicht"
        # - BMI von 25 bis unter 30: "Übergewicht"
        # - BMI ab 30: "Starkes Übergewicht"

# Gib am Ende den berechneten BMI und die Gewichtsklasse aus.

# Lösung

input("Willkommen zur Berechnung deines BMIs. Drücke Enter um fortzufahren.\n")

gewicht = float(input("Bitte gib dein Gewicht in KG an. Beispiel: 90.5\n"))
größe = float(input("\nBitte gib deine Körpergröße in Meter an. Beispiel: 1.90\n"))
BMI = gewicht/(größe**2)

if BMI <18.5:
    print("\nDein BMI beträgt:",BMI,"\nDu hast Untergewicht")
elif BMI <25:
    print("\nDein BMI beträgt:",BMI,"\nDu hast Normalgewicht")
elif BMI <30:
    print("\nDein BMI beträgt:",BMI,"\nDu hast Übergewicht")
else:
    print("\nDein BMI beträgt:",BMI,"\nDu hast starkes Übergewicht")

input("\nDrücke Enter um die Berechnung zu beenden.")

# ==============================================================================

# Aufgabe 2) Der Schaltjahr-Prüfer

# Ein Jahr ist nicht einfach alle vier Jahre ein Schaltjahr.
# Es gelten strengere Regeln. Schreibe ein Programm, das den Benutzer nach einer Jahreszahl fragt (int()) und prüft, 
# ob es sich um ein Schaltjahr handelt.

# Die Regeln für ein Schaltjahr sind:
#   - Ein Jahr ist ein Schaltjahr, wenn es restlos durch 4 teilbar ist.
#   - Ausnahme: Ist es auch restlos durch 100 teilbar, ist es kein Schaltjahr...
#   - Ausnahme von der Ausnahme: Es sei denn, es ist auch restlos durch 400 teilbar, dann ist es doch ein Schaltjahr.

# Setze diese Logik mit if, elif und else (oder einer cleveren Kombination mit and / or) um. 
# Der Modulo-Operator % hilft dir zu prüfen, ob eine Zahl restlos teilbar ist.
 
# Testwerte für dein Programm:
# 2024 → Schaltjahr (durch 4 teilbar)
# 2100 → Kein Schaltjahr (durch 4 und 100 teilbar, aber nicht durch 400)
# 2000 → Schaltjahr (durch 4, 100 und 400 teilbar)

# Lösung

# input("Willkommen zu deinem Schaltjahr-Prüfer. Drücke Enter um zu starten")

# jahr = int(input("\nBitte gib dein Jahr an um zu überprüfen, ob es ein Schaltjahr ist.\n"))

# if jahr % 400 == 0:
#     print("\nDas Jahr",jahr,"ist ein Schaltjahr\n")
# elif jahr % 100 == 0:
#     print("\nDas Jahr",jahr,"ist kein Schaltjahr\n")
# elif jahr % 4 == 0:
#     print("\nDas Jahr",jahr,"ist ein Schaltjahr\n")
# else:
#     print("\nDas Jahr",jahr,"ist kein Schaltjahr\n")

# input("Drücke Enter zum beenden.")

# ==============================================================================