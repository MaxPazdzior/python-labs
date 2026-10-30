# ==============================================================================

# ÜBUNGSAUFGABE 01: Zahlen filtern und summieren
# Sie haben eine Liste mit verschiedenen Zahlen vorliegen:
# zahlen = [3, 12, 7, 18, 5, 22, 9, 14]

# Aufgabenstellung:
# 1. Schreiben Sie ein Programm, das diese Liste durchläuft.
# 2. Geben Sie nur die Zahlen auf dem Bildschirm aus, die GRÖSSER ALS 10 sind.
# 3. Berechnen Sie gleichzeitig die SUMME aller Zahlen, die größer als 10 sind,
#    und geben Sie dieses Gesamtergebnis am Ende aus.

# Lösung

zahlen = [3, 12, 7, 18, 5, 22, 9, 14]

grosse_zahlen = []

for i in zahlen:
    if i > 10:
        grosse_zahlen.append(i)
print(f"Zahlen die größer als 10 sind, sind: {grosse_zahlen}\nDie Summe aller großen Zahlen ist: {sum(grosse_zahlen)}")

# ==============================================================================

# ÜBUNGSAUFGABE 02: Produkte nach Anfangsbuchstaben filtern

# Sie haben eine Liste mit Artikeln aus einem Supermarkt:
# produkte = ["Apfel", "Banane", "Ananas", "Erdbeere", "Avocado", "Kiwi"]

# Aufgabenstellung:
# 1. Schreiben Sie ein Programm, das diese Liste durchläuft.
# 2. Filtern Sie die Liste und geben Sie nur die Produkte aus, die mit dem 
#    Buchstaben "A" beginnen.
# 3. Zählen Sie, wie viele Produkte das insgesamt sind, und geben Sie die Anzahl 
#    am Ende aus.

# Lösung


# ==============================================================================

# ÜBUNGSAUFGABE 03: Passwörter auf Sicherheit prüfen
# Eine Website prüft, welche Passwörter von Usern sicher genug sind (mindestens 8 Zeichen):
# passwoerter = ["12345", "geheimnis123", "password", "abc", "sicheres_pwd_2026"]

# Aufgabenstellung:
# 1. Schreiben Sie ein Programm, das diese Liste durchläuft.
# 2. Geben Sie alle Passwörter aus, die ZU KURZ sind (also weniger als 8 Zeichen haben).
# 3. Zählen Sie, wie viele unsichere Passwörter in der Liste sind, und geben Sie die 
#    Zahl am Ende aus.

# ==============================================================================
