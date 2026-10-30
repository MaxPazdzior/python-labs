# ==============================================================================

# Aufgabe 1)

# Szenario: Ein Temperatursensor in einem Gewächshaus hat durch Funkstörungen
# fehlerhafte Extremwerte aufgezeichnet. Alle Werte über 40.0 Grad sind unrealistisch.
# Finde diese Ausreißer direkt in der Originalliste und deckele sie auf
# das Maximum von 40.0 Grad.

# Lösung
# Variante 1: Zählschleife

# temperaturen = [24.5, 42.1, 23.8, 55.0, 25.2, 40.0]

# for i in range (len(temperaturen)):
#     if temperaturen[i] >40.0:
#         print(f"Ausreißer gefunden bei Index {i} ({temperaturen[i]}°C) --> Korrigiert!")
#         temperaturen[i] = 40.0
# print("Bereinigte Temperaturen:", temperaturen)

# ==============================================================================

#Variante 2: Elementschleife, Ohne Index-Zugriff 

# temperaturen = [24.5, 42.1, 23.8, 55.0, 25.2, 40.0]
# temperaturen_fixed = []

# for temperatur in temperaturen:
#     if temperatur > 40.0:
#         temperaturen_fixed.append(40.0)
#     else:
#         temperaturen_fixed.append(temperatur)

# print("Bereinigte Temperaturen (Variante 2): ", temperaturen_fixed)

# ==============================================================================

# Aufgabe2)

# Variante 1: Der klassische Weg (Index)

# produkte = ["Kaffee", "Muffin", "Apfel"]
# preise = [3.50, 2.20, 0.80]

# print("\n--- Kassenbon ---")
# for i in range(len(preise)):
#     print(f"- {produkte[i]:10}: {preise[i]:.2f}€")      # --> :10 bedeutet, dass der abstand in der Konsole 10 Zeichen Abstand hat. --> :.f bedeutet 2 stellen nach dem Komma werden angezeigt.

# ==============================================================================

# Variante 2: Elementschleife - zip()

# produkte = ["Kaffee", "Muffin", "Apfel"]
# preise = [3.50, 2.20, 0.80]

# print("\n--- Kassenbon ---")
# for produkt, preis in zip(produkte, preise):
#     print(f"- {produkt:10}: {preis:.2f}€")

# ==============================================================================

# Gegeben ist eine Liste mit fortlaufenden Aktienkursen (Ganzzahlen):
# aktienkurse = [100, 102, 101, 105, 105, 108]
# Vergleichen Sie jeden Kurs ab dem zweiten Eintrag mit seinem direkten Vortag.
 
# Kursanstieg: Wenn der aktuelle Kurs höher als der Vortagskurs ist, berechnen Sie die Differenz. Geben Sie die Veränderung in EUR sowie den aktuellen Kurs im Format: 
# "Tag X: Kurs ist gestiegen! (+X EUR)"
# Kursabfall: Wenn der aktuelle Kurs niedriger als der Vortagskurs ist, geben Sie die Information im Format "Tag X: Kurs ist gefallen"
# Stagnation: Wenn der Kurs unverändert bleibt, geben Sie das Format "Tag X: Kurs ist gleich geblieben."

# Lösung

aktienkurse = [100, 102, 101, 105, 105, 108]

for index in range(1, len(aktienkurse)):
    aktueller_kurs = aktienkurse[index]
    vortages_kurs = aktienkurse[index - 1]
    differenz = aktueller_kurs - vortages_kurs
    
    tag = index + 1
    
    if differenz > 0:
        print(f"Tag {tag}: Kurs ist gestiegen! (+{differenz} EUR)")
    elif differenz < 0:
        print(f"Tag {tag}: Kurs ist gefallen")
    else:
        print(f"Tag {tag}: Kurs ist gleich geblieben.")

# ==============================================================================