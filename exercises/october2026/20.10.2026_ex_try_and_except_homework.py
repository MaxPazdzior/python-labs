# ==============================================================================

# Hausaufgabe 01: Ein Sensor-Data-Processor
 
# Du erhältst eine Liste von Messdaten (Dictionaries), die von einem Wettersensor stammen. Leider ist der Sensor alt und liefert manchmal fehlerhafte Daten:
# • Manchmal fehlt ein Schlüssel komplett.
# • Manchmal ist der Wert keine Zahl, sondern Text (z. B. "Error").
# • Am Ende soll der Mittelwert aller gültigen Temperaturen berechnet werden.
 
# Deine Programmier-Aufgabe:
 
# Schreibe eine Schleife, die die Sensordaten einzeln durchläuft, sie validiert und die gültigen Temperaturen in eine neue Liste filtert. 
# Sichere das Programm gegen folgende fünf Fehlerquellen ab:
# 1. Fehlender Daten-Schlüssel: Ein Wörterbuch enthält den Schlüssel "temperatur" überhaupt nicht. Typischer Fehler: KeyError
# 2. Falscher Datentyp im Datensatz: Der Wert hinter "temperatur" ist ein String (z. B. "DEFEKT"), der sich nicht in eine Zahl umwandeln lässt. 
# Typischer Fehler: ValueError
# 3. Extreme Ausreißer (Unrealistische Werte): Der Sensor liefert physikalisch unmögliche Werte (z. B. -274 Grad oder 1000 Grad). 
# Löse hierfür einen eigenen ValueError mittels raise aus.
# 4. Keine gültigen Daten vorhanden: Wenn am Ende keine einzige Temperatur gültig war, führt die Berechnung des Mittelwerts (Summe geteilt durch Anzahl) 
# zu einer Division durch Null. Typischer Fehler: ZeroDivisionError
# 5. Genereller Systemfehler: Ein unvorhergesehener Fehler tritt auf. Fange diesen ganz am Ende mit einem allgemeinen except Exception ab.
 
 
# Python
# # Die (teilweise beschädigten) Sensordaten
messdaten = [
    {"id": 1, "temperatur": 21.5},
    {"id": 2, "temperatur": "23.0"},     # Als String gespeichert (muss umgewandelt werden)
    {"id": 3, "temperatur": "DEFEKT"},   # Komplett falscher Datentyp
    {"id": 4},                           # Schlüssel "temperatur" fehlt völlig!
    {"id": 5, "temperatur": -300.0},     # Physikalischer Unsinn (unter dem absoluten Nullpunkt)
    {"id": 6, "temperatur": 18.2}
]

# Lösung

gültige_werte = []

for daten in messdaten:
    try:
        try:
            temp = float(daten["temperatur"])
        except ValueError:
            print("Die Temperatur ist keine gültige Zahl")
            continue
        if temp <-273 or temp >1000:
            raise ValueError("Die Werte sind unrealistisch prüfe das Thermometer")
        gültige_werte.append(temp)
    except KeyError:
        print("Der Wert Temperatur existiert nicht")
    except ValueError:
        print("Die Temperatur ist unrealistisch und wird desshalb nicht berücksichtigt")
    except Exception:
        print("Ein unvorhergesehender Systemfehler ist aufgetreten")
print(f"Die gültigen Werte, welche gefunden wurden sind: {gültige_werte}")

try:
    if len(gültige_werte) >0:
        mittelwert = sum(gültige_werte) / len(gültige_werte)
        print(f"Der Mittelwert aller Temperaturen ist: {mittelwert:.2f}")
    else:
        print("Es wurden keine Temperaturen hinterlegt")
except ZeroDivisionError:
        print("Es sind keine gültigen Daten vorhanden")
except Exception:
    print("Ein unvorhergesehender Systemfehler ist aufgetreten")

# ==============================================================================