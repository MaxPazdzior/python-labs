# ==============================================================================

# Aufgabe 0A (Leicht):
# Schreibe eine Funktion namens verdopple_zahl(zahl), die eine Zahl als Parameter
# übergeben bekommt. Sie soll diese Zahl mit 2 multiplizieren und das Ergebnis
# in einem kurzen Satz ausgeben.
 
# Beispiel-Aufruf: verdopple_zahl(5)
# Gewünschte Ausgabe: Das Doppelte von 5 ist 10.

# Lösung

# def verdopple_zahl(zahl):
#     antwort = zahl * 2
#     print(f"Das Doppelte von {zahl} ist {antwort}")

# verdopple_zahl(5)


# ==============================================================================

# Aufgabe 0B (Leicht): Noten-Check
 
# Schreibe eine Funktion namens pruefe_note(punkte).
# Wenn die Punktzahl 50 oder mehr beträgt, soll die Funktion "Bestanden!" ausgeben.
# Wenn die Punktzahl weniger als 50 beträgt, soll
# "Leider nicht bestanden." ausgegeben werden.
 
# Beispiel-Aufruf: pruefe_note(65)
# Gewünschte Ausgabe: Bestanden!

# Lösung

# def pruefe_note(punkte):
#     if punkte >=50:
#         print("Bestanden")
#     else:
#         print("Leider nicht bestanden.")

# pruefe_note(49)

# ==============================================================================

# Aufgabe 0C (Leicht): Die kleinere Zahl anzeigen
 
# Schreibe eine Funktion namens zeige_kleinere(zahl1, zahl2),
# die zwei Zahlen als Parameter erhält. Die Funktion soll prüfen,
# welche der beiden Zahlen kleiner ist, und diese mit einem kurzen Text ausgeben.
# (Aufpassen: Falls beide Zahlen gleich groß sind...?).
 
# Beispiel-Aufruf: zeige_kleinere(8, 3)
# Gewünschte Ausgabe: Die kleinere Zahl ist 3.

# Lösung

# def zeige_kleinere(zahl1, zahl2):
#     if zahl1 < zahl2:
#         print(f"Die kleinere Zahl ist {zahl1}.")
#     elif zahl1 > zahl2:
#         print(f"Die kleinere Zahl ist {zahl2}.")
#     else:
#         print("Die beiden Zahlen sind gleich groß.")

# zeige_kleinere(6,6)

# ==============================================================================

# Aufgabe 1: Supersportwagen-Check
 
# Schreibe eine Funktion namens ist_supersportwagen(ps, beschleunigung).
# Sie erhält zwei Werte:
# - ps: Die Leistung des Autos in PS (eine ganze Zahl).
# - beschleunigung: Die Zeit von 0 auf 100 km/h in Sekunden (eine Kommazahl, z. B. 3.2).
 
# Ein Auto gilt in diesem Spiel als Supersportwagen, wenn es mindestens 500 PS hat
# UND in unter 4.0 Sekunden von 0 auf 100 km/h beschleunigt.
# Wenn beide Bedingungen erfüllt sind, soll die Funktion True zurückgeben.
# Wenn eine oder beide Bedingungen nicht erfüllt sind, soll sie False zurückgeben.
 
# Beispiel-Aufruf 1:
# ist_supersportwagen(610, 3.2) → gibt True return (z. B. Audi R8).
 
# Beispiel-Aufruf 2:
# ist_supersportwagen(333, 4.6) → gibt False return (z. B. VW Golf R).

# Lösung

# def ist_supersportwagen(ps, beschleunigung):
#     if ps >=500 and beschleunigung <4.0:
#         return True
#     else:
#         return False

# ist_supersportwagen(500,4.0)

# ==============================================================================

# Aufgabe 2: Einkaufszettel-Rechner
 
# Es soll eine Python-Funktion namens einkauf_berechnen entwickelt werden.
# Die Funktion soll den Gesamtpreis eines Einkaufszettels berechnen,
# dabei automatisch teurere Artikel herausfiltern und am Ende ein Budget-Limit prüfen.
 
# Parameter: Die Funktion erhält zwei Werte:
# Eine Liste von Preisen (Dezimalzahlen) und ein maximales Budget (Zahl).
 
# Filterung: Preise, die höher als 50 Euro sind, sollen als "Spontankauf"
# ignoriert und nicht zum Gesamtpreis addiert werden.
 
# Budget-Check: Am Ende prüft die Funktion, ob der Gesamtpreis der erlaubten
# Artikel innerhalb des Budgets liegt.
 
# Die Funktion gibt "Einkauf erfolgreich!" aus, wenn das Budget ausreicht.
# Sie gibt "Budget überschritten!" aus, wenn die Gesamtsumme größer als das Budget ist.
 
# # TESTFÄLLE ZUM PRÜFEN:
# meine_preise = [10.50, 120.00, 25.00, 5.99, 65.00, 8.50] 
# # (120.00 und 65.00 sollten ignoriert werden. Die Summe der anderen ist 49.99)
 
# print(einkauf_berechnen(meine_preise, 60))  # Sollte ausgeben: Einkauf erfolgreich!
# print(einkauf_berechnen(meine_preise, 40))  # Sollte ausgeben: Budget überschritten!

# Lösung

# def einkauf_berechnen(preise, budget):
#     preise_budget = []
#     for i in range(len(preise)):
#         if preise[i] <=50:
#             preise_budget.append(preise[i])

#     summe = sum(preise_budget)
            

#     if summe <= budget:
#         print("Einkauf erfolgreich!")
#     else:
#         print("Budget überschritten!")

# preise = [10.50, 120.00, 25.00, 5.99, 65.00, 8.50]
# budget = 50
# einkauf_berechnen(preise,budget)

# ==============================================================================

# Aufgabe 3: Ein interaktives Kino-Buchungssystem
 
# Es soll ein Programm geschrieben werden, mit dem Kinobesucher freie 
# Sitzplätze (Nummern von 1 bis 10) buchen können.
# Bereits besetzte Plätze dürfen nicht doppelt gebucht werden.
 
# Anforderungen an die Funktion platz_buchen:
# Die Funktion erhält die gewünschte Sitzplatznummer (Zahl)
# und die Liste der bereits belegten Plätze.
 
# Gültigkeitsprüfung: Es sind nur die Plätze 1 bis 10 erlaubt.
 
# Verfügbarkeitsprüfung: Ist der Platz noch frei, wird er der Liste der
# belegten Plätze hinzugefügt und die Funktion gibt True zurück.
# Ist der Platz schon besetzt oder ungültig, gibt die Funktion False zurück.
 
# Das Hauptprogramm: Eine while-Schleife läuft so lange,
# bis das Kino voll ist (10 Plätze) oder der Benutzer "ende" eingibt.

# Lösung

def platz_buchen(zahl, belegte_plätze):
        if zahl >=1 and zahl <=10:
            if zahl in belegte_plätze:
                print("Dieser Platz ist bereits besetzt.")
                return False
            else: 
                belegte_plätze.append(zahl)
                return True
        else:
            print("Ungültige Platznummer.")
            return False
        

belegte_plätze = []

while len(belegte_plätze) <10:
     eingabe = (input("Bitte gib eine Zahl an\n"))
     if eingabe == "ende":
          print("Tschüss")
          break
     else: 
        zahl = int(eingabe)
        if platz_buchen(zahl,belegte_plätze):
             print(f"Platz {zahl} wurde gebucht.")

if len(belegte_plätze) == 10:
     print("Das Kino ist voll!")
        
# ==============================================================================