# ==============================================================================

# Hausaufgabe 02: Der Rabatt-Rechner
# Sie haben eine Liste mit Produktpreisen im Laden. Da Ausverkauf ist, soll jeder Preis, der über 50 Euro liegt, um 10 Euro reduziert werden:
# preise = [25.00, 65.00, 120.00, 45.00, 55.00, 10.00]
# Schreiben Sie ein Programm, das die Liste mit einer Schleife durchläuft. Ziehen Sie von jedem Wert, der größer als 50 ist, genau 10 ab. 
# Geben Sie die aktualisierte Liste am Ende komplett aus.

# Lösung

# preise = [25.00, 65.00, 120.00, 45.00, 55.00, 10.00]

# for i in range(len(preise)):
#     if preise[i] > 50.0:
#         preise[i] -= 10.0
# print(f"Die akutallisiert Liste ist: {preise}")

# ==============================================================================

# Hausaufgabe 03: Fitness-Tracker
# Gegeben ist eine Liste mit den täglichen Schrittzahlen einer Person über eine Woche (Ganzzahlen):
 
# schritte = [7500, 8200, 8200, 6100, 10500, 9800, 11000]
 
# Vergleichen Sie jeden Tag ab dem zweiten Eintrag mit dem direkten Vortag. Anforderungen:
# 1. Wenn die Schrittzahl höher ist als am Vortag, berechnen Sie die Differenz. Geben Sie das Ergebnis im Format aus: "Tag X: Zielstrebig! (+X Schritte)"
# 2. Wenn die Schrittzahl niedriger ist als am Vortag, geben Sie das Format aus: "Tag X: Weniger Bewegung als gestern."
# 3. Wenn die Schrittzahl exakt gleich geblieben ist, geben Sie das Format aus: "Tag X: Exakt dieselbe Schrittanzahl."

# Lösung

# schritte = [7500, 8200, 8200, 6100, 10500, 9800, 11000]

# for i in range(1,len(schritte)):
#     aktuelle_schritte = schritte[i]
#     vortags_schritte = schritte[i-1]
#     differenz = aktuelle_schritte - vortags_schritte

#     tag = i + 1

#     if differenz > 0:
#         print(f"Tag {tag}: Zielstrebig! (+{differenz} Schritte!)")
#     elif differenz < 0:
#         print(f"Tag {tag}: Weniger bewegung als gestern!")
#     else:
#         print(f"Tag {tag}: Exakt dieselbe Schrittzahl.")

# ==============================================================================

# Hausaufgabe 04: Server-Raum-Temperatur
# Ein Rechenzentrum zeichnet stündlich die Temperatur (in Grad Celsius) eines Server-Raums auf. 
# Wenn die Temperatur zu hoch wird oder zu schnell steigt, muss das System reagieren. 
# Gegeben ist die folgende Liste für einen Nachmittag:
 
# temperaturen = [21.5, 22.0, 24.5, 24.5, 26.0, 23.5, 24.0]
 
# Vergleichen Sie jede Temperatur ab dem zweiten Eintrag (Stunde 2) mit der direkten Vorstunde.
# Anforderungen:
# 1. Wenn die Temperatur steigt, berechnen Sie die Differenz.
# 	• Zusatzbedingung: Wenn der Anstieg 2.0 Grad oder mehr beträgt, geben Sie aus: "Stunde X: Warnung! Schneller Temperaturanstieg! (+X °C)"
# 	• Bei einem normalen Anstieg (unter 2.0 Grad) geben Sie aus: "Stunde X: Temperatur steigt leicht. (+X °C)"
# 2. Wenn die Temperatur fällt, geben Sie aus: "Stunde X: Kühlung läuft."
# 3. KWenn die Temperatur gleich bleibt, geben Sie aus: "Stunde X: Temperatur stabil."
# 4. Zählen Sie im Hintergrund mit, wie oft eine Warnung ausgelöst wurde. 
# Geben Sie ganz am Ende (nachdem die Schleife komplett fertig ist) das Gesamtergebnis aus, zum Beispiel: "Gesamtanzahl Warnungen: X"

# Lösung

# temperaturen = [21.5, 22.0, 24.5, 24.5, 26.0, 23.5, 24.0]

# warnung = 0

# for i in range(1,len(temperaturen)):
#     aktuelle_temp = temperaturen[i]
#     alte_temp = temperaturen[i-1]
#     differenz = aktuelle_temp - alte_temp

#     if differenz >0:
#         if differenz >2:
#             warnung +=1 
#             print(f"Stunde {i}: Warnung! Schneller Temperaturanstieg! (+{differenz}°C)")
#         elif differenz <2:
#             print(f"Stunde {i}: Temperatur steigt leicht. +{differenz}°C")
#     elif differenz <0:
#         print(f"Stunde {i}: Kühlung läuft.")
#     else:
#         print(f"Stunde {i}: Temperatur Stabil.")
# print(f"Gesamtzahl Warnungen: {warnung}")

# ==============================================================================