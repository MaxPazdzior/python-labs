# ==============================================================================

# Hausaufgabe 01: Validierung von Geschäftszeiten

# Ein Kundenservice-Unternehmen möchte seinen Chatbot optimieren.
# Der Bot soll automatisch erkennen, ob eine Kundenanfrage innerhalb oder außerhalb der regulären Geschäftszeiten eingeht, 
# um entweder direkt zu antworten oder eine Abwesenheitsnotiz zu senden.
# Die Kernarbeitszeit des Unternehmens liegt zwischen 08:00 Uhr (inklusiv) und 17:00 Uhr (inklusiv).
# • Liegt die Zeit im Zeitfenster, soll auf der Konsole ausgegeben werden: "Wir haben geöffnet! Wie können wir helfen?"
# • Liegt die Zeit außerhalb, soll ausgegeben werden: "Schon Feierabend. Bitte hinterlassen Sie eine Nachricht."

# Hinweis: Denken Sie daran, dass Sie für den reinen Uhrzeit-Vergleich keine Datumsangaben benötigen. Die Methode .time() eines datetime-Objekts ist hierbei sehr hilfreich.

# Lösung

import datetime as dt

begin = dt.time(hour=8, minute=0, second=0)
end = dt.time(hour=14, minute=0, second=0)
now = dt.datetime.now().time().replace(microsecond=0)

if now < begin or now > end:
    print(f"Schon Feierabend. Bitte hinterlassen Sie eine Nachricht.\nWir sind wieder ab: {begin} Uhr für sie da!")
else:
    print("Wir haben geöffnet! Wie können wir helfen?")

# ==============================================================================

# Hausaufgabe 02:

# In der Buchhaltungssoftware eines Online-Shops sollen Rechnungen automatisch überwacht werden.
# Kunden haben ab dem Rechnungsdatum exakt 14 Tage Zeit, um den Betrag zu begleichen.
# Geht bis dahin kein Geld ein, muss das System prüfen, seit wie vielen Tagen die Rechnung bereits überfällig ist, um die passende Mahnstufe einzuleiten.

# Das Rechnungsdatum liegt als Text im Format "Tag.Monat.Jahr" vor (z. B. "26.10.2026"). Konvertieren Sie diesen String in ein datetime-Objekt.

# Addieren Sie genau 14 Tage zum Rechnungsdatum, um das Zahlungsziel zu ermitteln.
# Vergleichen Sie das Zahlungsziel mit dem heutigen Datum (datetime.now()).

# Ausgabe:
# • Ist die Frist noch nicht abgelaufen, geben Sie aus, bis wann der Kunde Zeit hat: "Die Rechnung ist ausstehend. Zahlungsziel: DD.MM.YYYY."
# • Ist die Frist heute abgelaufen oder überfällig, berechnen Sie die Anzahl der Verzugstage und geben Sie aus: "Die Rechnung ist seit X Tagen überfällig!"

# Hinweis:
# Da datetime.now() auch Stunden und Minuten enthält, für die Frist aber nur der Kalendertag zählt, 
# sollten Sie die Objekte vor dem Vergleich mit .date() bereinigen oder die Uhrzeiten ignorieren.

# Lösung

rechnungsdatumstring = "26.10.2026"
rechnungsdatumundzeit = dt.datetime.strptime(rechnungsdatumstring, "%d.%m.%Y")
rechnungsdatum = rechnungsdatumundzeit.date()

todaydatumundzeit = dt.datetime.now()
today = todaydatumundzeit.date()

zahlungsziel = rechnungsdatum + dt.timedelta(days=14)

if today < zahlungsziel:
    print(f"Die Rechnung ist ausstehend. Zahlungsziel: {zahlungsziel.strftime('%d.%m.%Y')}.")
else:
    verzug = today - zahlungsziel
    verzugtage = verzug.days
    print(f"Die Rechnung ist seit {verzugtage} Tagen überfällig!")

# ==============================================================================
