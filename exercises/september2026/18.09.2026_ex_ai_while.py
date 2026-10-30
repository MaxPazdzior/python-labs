# ==============================================================================

# Aufgabe 1: Verdoppeln statt Runterzählen (Multiplikation in der Schleife)

# Ziel: Verstehen, wie sich Variablen in einer `while`-Schleife durch Multiplikation verändern.

# Schreibe ein Programm mit einer `while`-Schleife, das bei der Zahl `1` startet. 
# In jedem Schleifendurchlauf soll sich die Zahl verdoppeln ($1, 2, 4, 8, \dots$).

# Gib die Zahl in jedem Durchlauf aus. Die Schleife soll stoppen, sobald die Zahl **größer als 100** wird.

# Lösung

a = 1
while a <= 100:
    print(a)
    a *= 2

# ==============================================================================

# Aufgabe 2: Werte aufsummieren statt nur zählen

# Ziel: Kombination aus Schleife, Modulo-Bedingung (`%`) und dem Aufsummieren von tatsächlichen Zahlenwerten (statt nur einen Zähler um 1 zu erhöhen).

# Schreibe ein Programm, das alle Zahlen von **1 bis 40** (einschließlich) durchgeht.
# Berechne die **Gesamtsumme** aller Zahlen, die durch **4 teilbar** sind, aber **nicht durch 8** teilbar sind.

# Hinweis:

# Nutze eine Variable gesamtsumme = 0 und addiere die jeweilige Zahl darauf (`gesamtsumme += zahl`), wenn die Bedingung zutrifft.
# Nicht teilbar durch 8 bedeutet: `zahl % 8 != 0`.

# Lösung

zahl = 1
gesamtsumme = 0

while zahl <=40:
    if zahl % 4 == 0 and zahl % 8 != 0:
        gesamtsumme += zahl
    zahl += 1
print(gesamtsumme)

# ==============================================================================

# Aufgabe 3: Der PIN-Code-Checker (Bedingter Abbruch mit Rückmeldung)

# Ziel: Endlosschleife while True mit Eingabe-Überprüfung und unterschiedlicher Ausgabe je nach Eingabe.

# Schreibe ein Programm, das den Benutzer in einer Schleife nach einer PIN fragt input.

# Wenn die Eingabe nicht 1234 lautet, gibt das Programm aus: Falsche PIN, versuche es nochmal! und die Schleife läuft weiter.
# Wenn die Eingabe 1234 lautet, gibt das Programm aus: Zugriff gewährt! und beendet die Schleife mit break.

# Lösung

while True:
    pin = input("Bitte gib den gültigen Pin ein:\n")
    if pin == "1234":
        print("Zugriff gewährt!")
        break
    else:
        print("Falscher Pin, versuch es nochmal!")

# ==============================================================================

# Aufgabe 1: Der Countdown zum Raketenstart

# Ziel: Rückwärtszählen in variablen Schritten und eine Aktion nach Schleifenende ausführen.

# Schreibe ein Programm, das bei der Zahl 15 startet und in einer while-Schleife immer um 3 herunterzählt (15, 12, 9...).
# Gib jede Zahl in der Schleife aus. Die Schleife stoppt, sobald die Zahl kleiner als 0 wird.
# Nach Ablauf der Schleife soll genau einmal der Text "Start!" ausgegeben werden.

# Lösung

a = 15
while a >=0:
    print(a)
    a -= 3
print("Start!")

# ==============================================================================

# Aufgabe 2: Summe aller ungeraden Zahlen

# Ziel: Schleife, Modulo-Bedingung für ungerade Zahlen (% 2 != 0) und Aufsummieren von Werten.

# Schreibe ein Programm, das alle Zahlen von 1 bis 25 (einschließlich) durchgeht.
# Berechne die Gesamtsumme aller ungeraden Zahlen in diesem Bereich (Zahlen, die bei zahl % 2 != 0 wahr sind).
# Gib am Ende das Gesamtergebnis aus.

# Lösung

a = 1
gesamtsumme = 0

while a <=25:
    if a % 2 != 0:
        gesamtsumme += a
    a += 1
print(gesamtsumme)

# ==============================================================================

# Aufgabe 3: Der Einkaufszettel-Zähler

# Ziel: Endlosschleife while True mit Benutzereingabe, Zähler-Variable und Abbruchbedingung.

# Schreibe ein Programm, das den Benutzer in einer Schleife nach Einkaufsartikeln fragt input().
# Zähle mit einer Variable anzahl mit, wie viele Artikel eingegeben wurden.
# Wenn der Benutzer das Wort "ende" eingibt, bricht die Schleife mit break ab.
# Gib am Ende aus, wie viele Artikel insgesamt eingegeben wurden (das Wort "ende" darf nicht mitgezählt werden!).

# Lösung

liste = []
summe = 0
while True:
    eingabe = input("Gib deine Artikel für den Einkauf ein!\n")
    if eingabe == "ende":
        break
    elif eingabe != "ende":
        liste.append(eingabe)
    summe +=1
print(f"Es wurden insgesammt {summe} Artikel erfasst.\n Undzwar: {liste}")

# ==============================================================================
