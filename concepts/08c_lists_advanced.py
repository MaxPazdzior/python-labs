# ==============================================================================

# Liste addieren:

a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
print(c)

# ==============================================================================

# Elemente vervielfachen

x = [0] * 10  # --> Sorgt dafür dass die "0" 10x in die Liste geschrieben wird
print(x)

# ==============================================================================

# Slicing als Zuwesiung

l1 = [5,2,7,5,8,1,0,]  # --> Hier wird von stelle 2 der Tabelle bis zur 5 Stelle ausgegeben aber nicht die 5 Stelle es geht nur bis dorthin!!
print(l1[2:5])

# ==============================================================================

# Elemnte ersetzten:

# l1[1:3] = [20,30]       # --> Hier wird die Zahl an Stelle 1 und 2 ( Nicht 3!!) durh die Zahlen ersetzt, die in der Liste stehen
# l1[1:5] = [20,30]
l1[1:5] = []  # --> Entfernt die Zahlen an den Stellen aus der Liste.
print(l1)

# ==============================================================================

# List Comprehension
# Syntax:
# [ausdruck for element in iterable if bedingung]

# 1. Einfache Liste
zahlen = [x for x in range(10)]  # --> Erstellt eine Liste von 0-9
print(zahlen)

# 2. Berechnungen
quadrate = [x**2 for x in range(1, 6)]  # --> "**" beduetet hier ^ also Hoch 2 oder 3. Hier wird jede Zahl von 1-6 hoch sich selbst genommen. Output: [1, 4, 9, 16, 25]
print(quadrate)

# 3. Filter mit if
gerade = [a for a in range(10) if a % 2 == 0]  # --> Hier wird wieder von 0-9 durchgegangen. "%" Modulo gibt nur die gerade zahlen aus wegen % 2
print(gerade)

# 4. String manipulieren
fruechte = ["apfel", "banane", "erdbeere"]
gross = [f.upper() for f in fruechte]   # --> Sorgt dafür, dass alle Buchstaben gross geschrieben werden
print(gross)

# 5. Datentypen konvertieren
str_zahlen = ["1","2","3","4","5"]
int_zahlen = [int(x) for x in str_zahlen]   # --> Hier werden die Zahlen als String in einen Integer umgewandelt 
print(int_zahlen)

# 6. if-else im Ausdruck
kategorien = ["gerade" if x % 2 == 0 else "ungerade" for x in range(5)]     # --> Hier werden die Zhalen von 0-4 geprüft ob sie gerade oder ungerade sind und so auch ausgegeben
print(kategorien)

# 7. Zeichenketten filtern
namen = ["Anna", "Ben", "Anton", "Christina"]
a_namen = [n for n in namen if n.startswith("A")]       # --> Hier wird eine Liste erstellt mit den Namen die nur mit A Anfangen
print(a_namen)

# 8. Länge von Elemten ermitteln
woerter = ["Python", "Code", "List"]
laengen = [len(w) for w in woerter]     # --> Zählt wie viele Buchstaben ein Wort hat und gibt diese Zahl aus
print(laengen)

# ==============================================================================

# enumerate()
# 1. Standardfall: Index und Elemente ausgeben
fruchte = ["Apfel", "Banane", "Mango"]

for index, frucht in enumerate(fruchte):
    print(f"Index: {index}, Frucht: {frucht}")

for i in range(0,len(fruchte)):
    print(f"Index: {i}, Frucht: {fruchte[i]}")      # --> Ist das gleiche wie darüber

# 2. Startindex anpassen
tiere = ["Hund", "Katze", "Vogel"]
for nummer, tier in enumerate(tiere, start=1):
    print(f"{nummer}. {tier}")

# 3. String durchnummerieren
wort = "Python"
for i, buchstabe in enumerate(wort):
    print(f"Position {i}: {buchstabe}")

# 4. Elemente verändern
werte = [10,20,30]

for index, wert in enumerate(werte):
    werte[index] = wert * 2
print(werte)

# ==============================================================================