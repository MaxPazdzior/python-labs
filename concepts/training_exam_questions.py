# ==============================================================================

# 1) Welcher Datentyp?

a = 42  # --> Integer
b = "42"    # --> String
c = 42  # --> Integer
d = True    # --> Bool
e = "False" # --> String
f = [1, 2, 3]   # --> Liste
g = {"name": "Anna","alter":35} # --> Dict
h = 3 + 4.5 # --> Float
i = 10/2    # --> Float
j = 10 >5   # --> Bool

# ==============================================================================

# 2) Welcher Datentyp?

a = 2 * 1.5 # --> Float
b = 17 // 5 # --> Int
c = 20 % 10 # --> Int
d = 5 % 3   # --> Int
e = int(2.3)    # --> Int
f = float("3.5")    # --> Float
g = len([3, 2, 1, 0])   # --> Int
h = str(55) # --> String
i = {}  # --> Dict
j = ["A", "B", "C"] # --> Liste

# ==============================================================================

# 3) Welcher Datentyp?

a = 3**2    # --> Int
b = not True    # --> Bool
c = "P" in "Python" # --> Bool
d = 1 == 2  # --> Bool
e = len("100")  # --> Int
f = 0.0 // 1    # --> Float
g = []  # --> Liste
h = 3 * "A" # --> String
i = [{"A": 1, "B": 2}]  # --> Liste
j = f"Name" # --> String

# ==============================================================================

# 4) Was wird ausgegeben?

a = "12"    # --> String
b = [4, 5, 6]   # --> List
c = True    # --> Bool 
print(type(a), type(b), type(c))

# ==============================================================================

# 1) Was wird ausgegeben?

a = 5
b = 3
c = a + b
d = c - 1
print(d)

# --> 7

# ==============================================================================

a = 1
b = 2
a += b
a += 1
print(a)

# --> 4

# ==============================================================================

# 3) Was wird ausgegeben?

a = 2
b = 3
a *= b
c = a + 1
print(c)

# --> 7

# ==============================================================================

# 4) Was wird ausgegeben?

a = 4
b = 4 / a
c = b * 3
d = 6 // 3
print(d)

# --> 2

# ==============================================================================

# 5) Was wird ausgegeben?

a = 1
b = 2
temp = b
b = a
a = temp
print(a, b)

# --> 2,1

# ==============================================================================

# 6) Was wird ausgegeben?

a = "1"
b = "2"
c = a + b
print(c)

# --> 12

# ==============================================================================

# 7) Was wird ausgegeben?

a = "x"
b = 5 * a
print(b)

# --> xxxxx

# ==============================================================================

# 8) Was wird ausgegeben?

a = True
b = False
print(a and b)

# --> False

# ==============================================================================

# 9) Was wird ausgegeben?

a = 4
b = 2
c = 4 % 2
print(c + 1)

# --> 1

# ==============================================================================

# 10) Was wird ausgegeben?

a = 4.0
b = 1.0
c = a + b
print(int(c))

# --> 5

# ==============================================================================

# Wofür steht die Abkürzung „EVA“ im Bereich der Informatik?

#  A) Eingabe, Verarbeitung, Ausgabe
#  B) Erweiterung, Verknüpfung, Analyse
#  C) Einsatz, Verarbeitung, Anwendung
#  D) Eingabe, Vervielfältigung, Auswertung

# --> A)

# ==============================================================================

# Was beschreibt eine „funktionale Anforderung“ an ein Softwaresystem am besten?

#  A) Wie schnell das System auf Benutzereingaben reagiert.
#  B) Welche konkreten Aufgaben und Funktionen das System ausführen muss.
#  C) Auf welchem Betriebssystem die Software laufen soll.
#  D) Wie hoch die Lizenzkosten für die Entwicklung sein dürfen.

# --> B)

# ==============================================================================

# Welche der folgenden Aussagen ist eine typische funktionale Anforderung für eine Banking-App?

#  A) Die App muss nach dem ISO-27001-Standard verschlüsselt sein.
#  B) Die App muss auf Android- und iOS-Geräten fehlerfrei laufen.
#  C) Der Nutzer muss eine Überweisung mit Empfängername, IBAN und Betrag ausführen können.
#  D) Die Benutzeroberfläche muss barrierefrei und für Sehbehinderte gut lesbar sein.

# --> C)

# ==============================================================================

# Welche Aussage trifft auf sogenannte „höhere Programmiersprachen“ (z. B. Python, Java oder C#) zu?

#  A) Sie bestehen ausschließlich aus Nullen und Einsen (Binärcode).
#  B) Sie sind stark an die menschliche Sprache angelehnt und abstrahieren die Hardware-Details.
#  C) Sie können ohne Übersetzung direkt vom Prozessor ausgeführt werden.
#  D) Sie lassen sich nur auf einem einzigen, spezifischen Prozessortyp ausführen.

# --> B)

# ==============================================================================

# Welche der folgenden Sprachen weist die geringste Abstraktionsebene auf und gilt daher als „hardwarenahe Programmiersprache“ (Low-Level)?

#  A) Python
#  B) SQL
#  C) Assembler
#  D) JavaScript

# --> C)

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if a > b:
    print("Hallo!")
else:
    print("Bye!")

# --> Hallo!

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if b >= c + 1:
    print("Grün")
else:
    print("Rot")

# --> Grün

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if a != c and b > d:
    print("Bayern")
else:
    print("Sachsen")

# --> Sachsen

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if c > d or a >= 4:
    print("A"*3)
else:
    print("B"*3)

# --> AAA

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if not c < d:
    print("Indiana")
else:
    print("Jones")

# --> Jones

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if a < 2:
    print("USA")
elif a == 2:
    print("Kanada")
elif b < 3:
    print("Mexico")
else:
    print("Not found!")

# --> Not found!

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if a >= 3:
    print("Tomato")
    if b < 10:
        print("Salat"*c)

# --> Tomato 
# --> SalatSalat

# ==============================================================================

a = 4
b = 3
c = 2
d = 5

if b > 1:
    b = 0
    if b == 0:
        print("Geschafft!!")
    print("*"*(b+5))
else:
    print("Nicht geschafft!")

# --> Geschafft!!
# --> *****

# ==============================================================================

# Endlich oder Endlos???

i = 0
while i < 5:
    print(i)
    i += 1

# --> Endlich

# ==============================================================================

# Endlich oder Endlos???

i = 0
while i < 5:
    print(i)

# --> Endlos

# ==============================================================================

# Endlich oder Endlos???

lauf = True
while lauf:
    print("Hallo")
    lauf = False

# --> Endlich

# ==============================================================================

# Endlich oder Endlos???

x = 10
while x > 0:
    x -= 2

# --> Endlich

# ==============================================================================

# Endlich oder Endlos???

x = 2
while x > 0:
    x += 1

# --> Endlos

# ==============================================================================

# Endlich oder Endlos???

zahl = 1
while zahl < 10:
    if zahl % 2 == 0:
        zahl += 1

# --> Endlos

# ==============================================================================

# Endlich oder Endlos???

geheimnis = 42
tipp = 0
while tipp != geheimnis:
    tipp += 5

# --> Endlos

# ==============================================================================

# Endlich oder Endlos???

while True:
    break
    print("Schleife läuft immer noch")

# --> Endlich

# ==============================================================================

# Was wird ausgegeben?

zeit = 3
while zeit > 0:
    print(zeit)
    zeit = zeit - 1
print("Start!")

# --> 3 
# --> 2 
# --> 1 
# --> Start!

# ==============================================================================

# Was wird ausgegeben?

zeit = 3
while zeit >= 0:
    zeit = zeit - 1
    print(zeit)
print("Start!")

# 2
# 1
# 0
# -1
# Start!

# ==============================================================================

# Was wird ausgegeben?

zahl = 10
while zahl < 100:
    if zahl % 10 == 0:
        print("Gefunden:", zahl)
        break
    zahl += 1

# --> Gefunden: 10

# ==============================================================================

# Was wird ausgegeben?

counter = 6
while counter > 0:
    counter -= 1
    if counter == 4:
        continue
    print(counter)

# 5 
# 4 
# 3 
# 2 
# 1 
# 0

# ==============================================================================

# Wettbewerb

zahl = 0
summe = 0
while zahl < 20:
    zahl += 1
    if zahl % 2 == 0:
        continue  # Gerade Zahlen überspringen
    summe += zahl
    if summe > 4:
        break
print(zahl)

# --> 5

# ==============================================================================

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

# ==============================================================================

for i in range(2,7):
    print(i)

# 2
# 3
# 4
# 5
# 6

# ==============================================================================

for i in range(0,10,2):
    print(i)

# 0
# 2
# 4
# 6
# 8

# ==============================================================================

wort = "Python"

for buchstabe in wort:
    print(buchstabe)

# P 
# y 
# t 
# h 
# o 
# n

# ==============================================================================

zahlen = [10,20,30]

for z in zahlen:
    print(z+5)

# 15
# 25
# 35

# ==============================================================================

for zahl in range(1,11):
    if zahl % 2 == 0:
        print(zahl)

# 2
# 4
# 6
# 8
# 10

# ==============================================================================

for i in range(1,3):
    for j in range(1,3):
        print(i*j)

# 1
# 2
# 2
# 4

# ==============================================================================

text = "Code"

for zeichen in text:
    if zeichen == "o":
        print("Gefunden.")
    else:
        print("Nein")

# Nein
# Gefunden
# Nein
# Nein

# ==============================================================================

namen = ["Max","Anna","Tom","Lisa"]

for name in namen:
    if len(name) > 3:
        print(name)
    else:
        print("Zu kurz")

# Zu kurz
# Anna
# Zu Kurz
# Lisa

# ==============================================================================

schalter = [True, False, True]

for s in schalter:
    if s:
        print("Licht an")
    else:
        print("Licht aus")

# Licht an
# Licht aus
# Licht an

# ==============================================================================

zahlen = [1,3,7,4,9]

for z in zahlen:
    if z % 2 == 0:
        print("Gefunden.")
        break
    else:
        print("Suche...")

# Suche...
# Suche...
# Suche...
# Gefunden

# ==============================================================================

daten = [5, None, 12, None, 8]

for d in daten:
    if d is None:
        continue
    else:
        print(d*2)

# 10
# 24 
# 16

# ==============================================================================

werte = [6,3,7,2,5,1]

print(werte[1])
print(werte[-1])
print(werte[0:3])
print(werte[:4])
print(werte[4:])

# 3
# 1
# 6, 3, 7
# 6, 3, 7, 2
# 5, 1

# ==============================================================================

aufgaben = ["Einkaufen", "Putzen", "Kochen"]

erledigt = aufgaben.pop()   # --> Wenn Klammer leer wird immer das letzte weg gemacht

print(erledigt)
print(aufgaben)

# Kochen
# Einkaufen, Putzen

# ==============================================================================

zutaten = ["Mehl", "Zucker", "Eier"]

print("Zucker" in zutaten)
print("Chocolate" in zutaten)
print("Marshmellow" not in zutaten)

# True
# False
# True

# ==============================================================================

fruechte = ["apfel", "banane", "erdbeere"]

for f in range(0,len(fruechte)):
    fruechte[f] = fruechte[f].upper()

print(fruechte[2])

# ERDBEERE

# ==============================================================================

punkte = [85, 42, 60, 38]

for i in range(len(punkte)):
    if punkte[i] >= 50:
        print(f"TN {i + 1}: Bestanden")
    else:
        print(f"TN {i + 1}: Durchgefallen")

# TN 1: Bestanden
# TN 2: Durchgefallen
# TN 3: Bestanden
# TN 4: Durchgefallen

# ==============================================================================

def begruessen(name):
    print(f"Hallo, {name}!")

begruessen("Anna")
begruessen("Tim")

# Hallo, Anna!
# Hallo, Tim!

# ==============================================================================

def quadrieren(zahl):
    return zahl * zahl

ergebnis = quadrieren(5) + quadrieren(2)
print(ergebnis)

# 29

# ==============================================================================

def pruefe_alter(alter):
    if alter < 0:
        return "Ungültiges Alter"
    if alter >= 18:
        return "Volljährig"
    return "Minderjährig"

print(pruefe_alter(20))
print(pruefe_alter(12))

# Volljährig
# Minderjährig

# ==============================================================================

def min_und_max(zahlen):
    return min(zahlen), max(zahlen)

kleinste, groesste = min_und_max([4, 9, 2, 7])
print(f"Min: {kleinste}, Max: {groesste}")

# Min:2 Max: 9

# ==============================================================================

def potenz(basis, exponent=2):
    return basis ** exponent

print(potenz(3))
print(potenz(2, 3))

# 9
# 8

# ==============================================================================

def verdoppeln(zahl):
    ergebnis = zahl * 2
    print(ergebnis)

x = verdoppeln(5)
print(x + 10)

# --> Fehler da print anstatt return

# ==============================================================================

def sage_hallo(name):
    return f"Hallo, {name}!"
    print("Funktion wurde ausgeführt.")

print(sage_hallo("Max"))

# Das print kommt nach dem return und wird so nicht ausgeführt

# ==============================================================================

def zeige_status():
    return "Alles okay"

print(zeige_status)

# Die Klammern fehlen im print

# ==============================================================================

def preis_berechnen(rabatt, preis):
    return preis - rabatt

print(preis_berechnen(50))

# Der Parameter in der Klammer hinter der 50 fehlt

# ==============================================================================
