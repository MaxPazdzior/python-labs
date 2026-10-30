# ==============================================================================

# Hausaufgabe 01: Geheimsprache
# Schreibe ein Programm, das einen Text Buchstabe für Buchstabe durchgeht.
# Jedes Mal, wenn das Programm auf ein kleines oder großes "e" oder "a" stößt,
# soll es stattdessen ein "*" (Sternchen) ausgeben. Alle anderen Buchstaben bleiben ganz normal.
 
# Beispiel: Aus "Erdbeere" wird "*rdb**r*"

# Lösung

wort = "Erbdbeere"
vokale = "EeAa"
neues_wort = ""

for i in wort:
    if i in vokale:
        neues_wort += "*"
    else:
        neues_wort += i
print(f"Altes Wort: {wort}\nNeues Wort: {neues_wort}")


# ==============================================================================

# Hausaufgabe 02: Gültige Klammerung prüfen
 
# Schreibe ein Programm, das prüft, ob in einem mathematischen Ausdruck oder einem Code-String die runden Klammern ( und ) korrekt geöffnet und geschlossen werden.
# Die Regeln:
# 1. Jede geschlossene Klammer ) braucht vorher eine geöffnete Klammer (.
# 2. Am Ende des Strings dürfen keine Klammern offenbleiben.
# 3. Ausdrücke wie ()() oder (()) sind gültig.
# 4. Ausdrücke wie )( (falsche Reihenfolge) oder (() (eine bleibt offen) sind ungültig.
 
# Beispiel: "(a + b) * (c - (d / e))" -> Korrekt

while True:
    text = input("Gib einen Text oder eine Mathegleichung ein, oder gebe exit ein zum beenden\n")

    if text == "exit":
        print("Auf wiedersehen!")
        break

    zaehler = 0
    gueltig = True

    for i in text:
        if i == "(":
            zaehler += 1
        elif i == ")":
            zaehler -= 1

        if zaehler < 0:
            gueltig = False
            break

    if zaehler != 0:
        gueltig = False

    if gueltig:
        print("Korrekt!")
    else:
        print("Ungültig!")

# ==============================================================================
