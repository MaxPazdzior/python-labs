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

datum = dt.date(year=1999,month=3,day=12)
print(datum)
heute = dt.date.today() # --> Gibt mir das heutige Datum
print(heute)
time_differenz = heute - datum  # --> Rechnet die Tage die bis heute vergangen sind
print(type(time_differenz))

# ============================================================================== 
