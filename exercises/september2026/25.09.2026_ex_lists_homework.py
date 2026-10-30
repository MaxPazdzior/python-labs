# =====================================================================

# Hausaufgabe 01: Der Sparbuch-Zähler

# Ein Sparbuch enthält eine Liste von Geldeingängen (positive Zahlen) und Geldausgängen (negative Zahlen):

# transaktionen = [50, -20, 100, -5, -30, 15]

    # Schreiben Sie ein Programm, das diese Liste analysiert.
    # Finden Sie heraus, wie viele Ausgänge (Zahlen kleiner als 0) es in der Liste gibt.
    # Berechnen Sie die Gesamtsumme aller Einzahlungen (nur die Zahlen größer als 0).
    # Geben Sie beide Ergebnisse auf dem Bildschirm aus.

# Lösung

transaktionen = [50, -20, 100, -5, -30, 15]

negativ_count = 0
summe = 0

for i in transaktionen:
    if i <0:
        negativ_count +=1
    elif i >0:
        summe += i 
print(f"Es gibt insgesamt {negativ_count} Negative Auszahlungen\nDie Summe aller Einzahlungen ergibt {summe}")


# =====================================================================

# Hausaufgabe 02: Namen filtern nach Länge

# Sie haben eine Liste mit verschiedenen Vornamen vorliegen:

# namen = ["Tom", "Anna", "Maximilian", "Eva", "Katharina", "Jan"]

    # Schreiben Sie ein Programm, das diese Liste durchläuft.
    # Geben Sie nur die Namen auf dem Bildschirm aus, die mehr als 4 Buchstaben haben.
    # Zählen Sie gleichzeitig, wie viele "große" Namen insgesamt sind, und geben Sie diese Zahl am Ende aus.
    # Tipp: Was macht die Funktion len("Mein Text hier drinnen...")?

# Lösung

namen = ["Tom", "Anna", "Maximilian", "Eva", "Katharina", "Jan"]

long_name = []

for i in namen:
    if len(i) > 4:
        long_name.append(i)
print(f"Die namen mit mehr als 4 Buchstaben sind: {long_name}\nEs sind insgesamt {len(long_name)} Namen.")

# =====================================================================
