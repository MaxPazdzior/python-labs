# ==============================================================================

import datetime as dt

# ==============================================================================

# Modul datetime: Menschliche Kalenderlogik (Tage, Wochen, Zeitzone)
# Zeitzone-Steuerung
# Ideal für: Datenbankeintrage, Terminplanungen, Fristen berechnen, Endnutzerformatierungen

# WICHTIG: Zeitpunkt vs. Zeitinterval

# TIMEDELTA: Representiert Zeitspanne oder Dauer (Zeitinterval)

# ============================================================================== 

duration = dt.timedelta(    # --> Wandelt alles in Tage und Stunden etc. um
    weeks = 12,
    days = 50,
    hours = 4,
    minutes = 2,
    seconds = 27,
    milliseconds = 45,
    microseconds = 12 
)
print(duration) # --> Gibt alles an
print(duration.days)    # --> Gibt nur die Tage an
print(duration.seconds) # --> Nur die Sekunden
print(duration.microseconds)    # --> Nur die Microsekunden
print(duration.total_seconds())

duration1 = dt.timedelta(weeks=4)
duration2 = dt.timedelta(days=22)
duration3 = dt.timedelta(weeks=1,days=4)
print(duration1 + duration2 + duration3)
print(duration1 * 5)

# ============================================================================== 

# DATE OBJECTS: Zeitpunkt

datum = dt.date(year=2020,month=9,day=29)
print(datum)
heute = dt.date.today() # --> Gibt mir das heutige Datum
print(heute)
time_differenz = heute - datum  # --> Rechnet die Tage die bis heute vergangen sind
print(time_differenz)

heute = heute.replace(year=2028)    # --> Jahr von heute wurde auf 2028 geändert. --> Bedenke: heute ist die variable die wir zugewiesen haben nicht das heutige Datum heute = ...
print(heute)

print(heute.weekday())  # --> Wochentag wird ausgegeben. / Monday is 0; Sunday is 6

# ==============================================================================

# Time Objects

t1 = dt.time(hour = 3, minute = 41, second = 12)    # --> Uhrzeit wird bestimmt
print(t1)
t2 = dt.time(hour = 3, minute = 41, second = 12, microsecond = 453)
print(t2)
print(t2.hour)  # --> Gibt nur die zuvor definierte Stunde aus

t3 = dt.time.min    # Mitternacht!
print(t3)

# ==============================================================================

# Datetime Objects

dt1 = dt.datetime(year=2021,month=2,day=3,hour=10,minute=13,second=45)  # --> Hier kann man dann alles zusammen bestimmen
dt2 = dt.datetime(2022,4,2,10,32)   # --> Wenn man die Reihenfolge beachtet kann man es auch so schreiben
print(dt1,dt2)
abstand = dt2 - dt1 # --> Differenz in Tage kann man so ausrechnen
print(abstand)
print(abstand.days / 365)   # --> Zeigt die Differenz im Jahr an

# ==============================================================================

# Konvertierung

date1 = dt1.date()    # --> Konvertierung datetime -> date
time1 = dt1.time()  # --> Konvertierung datetime -> time
print(f"{date1}\n{time1}")
dt3 = dt.datetime.combine(date1,time1)  # --> So kann man sie wieder zusammenfügen
print(dt3)

# ==============================================================================

# Text in "echtes" Datum umwandeln (Parsing)

datum_string = "24.12.2026 18:30"

# %d = Tag, %m = Monat, %Y = Jahr, %H = Stunde, %M = Minute
echtes_datum = dt.datetime.strptime(datum_string, "%d.%m.%Y %H:%M") # --> Unser String wird hier umgewandelt in ein Datetime Object
print(echtes_datum)

us_zeit = "11:45 PM"
parsed_zeit = dt.datetime.strptime(us_zeit, "%I:%M %p") # --> Amerikanische Zeit umwandeln
print(parsed_zeit)

print(f"24h-Format: {parsed_zeit.strftime("%H:%M")}")

# ==============================================================================

jahr, kw, wochentag = heute.isocalendar()
print(f"Wir befinden uns in der Kalenderwocher (KW):{kw}")

# ==============================================================================
