# ==============================================================================

# Aufgabe 01 

# Schreiben Sie ein Python-Skript, das den genauen Liefertermin
# für eine Bestellung berechnet. Gehen Sie dabei von einer festen
# Lieferzeit von 3 Tagen und 5 Stunden aus.
# Da am Wochenende keine Lieferungen stattfinden,
# müssen Liefertermine, die auf einen Samstag oder Sonntag fallen,
# automatisch auf den folgenden Montag verschoben werden.

# ==============================================================================

import datetime as dt

jetzt = dt.datetime.now()   # --> Datum von heute
lieferzeitspanne = dt.timedelta(days=3, hours=5)    # --> Lieferzeit v on 3 Tagen und 5 Stunden

liefertermin = jetzt + lieferzeitspanne

if liefertermin.weekday() == 5: # --> Weekday 5 = Samstag
    liefertermin += dt.timedelta(days=2)
elif liefertermin.weekday() == 6:   # --> Weekday 6 = Sonntag
    liefertermin += dt.timedelta(days=1)

print(liefertermin.strftime("%d.%m.%Y %H:%M:%S  (%A)")) # --> "%A" damit der Wochentag mit dort bei steht. 

# ==============================================================================
