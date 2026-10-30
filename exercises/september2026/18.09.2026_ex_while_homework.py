# ==============================================================================

# Hausaufgabe 1: 
# Zahlenreihen rückwärts ausgeben. Starte bei der Zahl 10. Zähle in der Schleife immer um 2 herunter (10, 8, 6...). 
# Die Schleife stoppt, sobald die Zahl kleiner als 0 wird.

# Lösung

a = 10
while a >0:
    print(a)
    a -=2

# ==============================================================================

# Hausaufgabe 2: 
# Schreibe ein Programm, das zählt, wie viele Zahlen zwischen 1 und 30 (einschließlich) sowohl durch 2 als auch durch 3 glatt teilbar sind.
# Hinweis: Eine Zahl erfüllt beide Bedingungen, wenn zahl % 2 == 0 und zahl % 3 == 0 ist.

# Lösung

zahl = 30
summe = 0
while zahl >= 1:
    if zahl % 2 == 0 and zahl % 3 == 0:
        summe += 1
    zahl -= 1
print(f"Zwischen 1 und 30 sind genau: {summe} Zahlen durch 2 und 3 glatt teilbar!")    

# ==============================================================================

# Hausaufgabe 3: 
# Der nervige Papagei! Lies mit input() ein Wort vom Benutzer ein. 
# Gib dieses Wort direkt wieder aus. Wiederhole das so lange, bis der Benutzer das Wort "tschüss" eingibt.

# Lösung

while True:
    wort = input("Was soll der Papagei sagen?\n")
    if wort == "tschüss":
        print("Papagei sagt: Hau rein!")
        break
    print(f"Papagei sagt: {wort}")

# ==============================================================================
