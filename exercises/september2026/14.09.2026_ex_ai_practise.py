# ==============================================================================

# Aufgabe 1: Der Kino-Ticket-Rechner (Leicht)

# Erstelle ein Python-Programm, das das Alter eines Kinobesuchers prüft und den entsprechenden Ticketpreis 
# auf dem Bildschirm ausgibt.

# Variable definieren:
# Erstelle eine Variable namens alter und weise ihr einen ganzzahligen Wert zu (z. B. 25).

# Bedingungen prüfen:
# Nutze eine if-elif-else-Struktur, um den Preis nach folgenden Regeln zu ermitteln:

        # - Ab 65 Jahren: Das Ticket kostet 8 Euro (Seniorentarif).

        # - Ab 18 Jahren: Das Ticket kostet 12 Euro (Erwachsenentarif).

        # - Ab 12 Jahren: Das Ticket kostet 6 Euro (Jugendtarif).

        # - Unter 12 Jahren: Das Ticket kostet 4 Euro (Kindertarif).

# Ausgabe berechnen:
# Das Programm soll den Preis auf dem Bildschirm ausgeben (z. B. "Das Ticket kostet: 12 Euro").

# Testen:
# Ändere das alter mehrmals manuell im Code (z. B. auf 70, 15 oder 8), um zu prüfen, ob das Programm richtig rechnet.

# Lösung

alter=11

if alter >=65:
    print("Das Ticket kostet 8€. Sie bekommen den Seniorentarif!")
elif alter >=18:
    print("Das Ticket kostet 12€. Sie müssen den Erwachsenentarif bezahlen!")
elif alter >=12:
    print("Das Ticket kostet 6€. Sie müssen den Jugendtarif bezahlen!")
else:
    print("Das Ticket kostet 4€. Sie müssen den Kindertarif bezahlen!")

# ==============================================================================

# Aufgabe 2: Der Kleider-Berater (Leicht)

# Erstelle ein Python-Programm, das anhand der aktuellen Außentemperatur eine passende Kleidungsempfehlung ausgibt.

# Variable definieren:
# Erstelle eine Variable namens temperatur und weise ihr einen ganzzahligen Wert zu (z. B. 18).

# Bedingungen prüfen:
# Nutze eine if-elif-else-Struktur, um das Wetter nach folgenden Regeln zu bewerten:

        # - Ab 25 Grad: "Zieh ein T-Shirt an, es ist heiß!"

        # - Ab 15 Grad: "Ein Pullover reicht aus."

        # - Ab 5 Grad: "Zieh dir eine warme Jacke an."

        # - Unter 5 Grad: "Es ist eiskalt, zieh den Wintermantel an!"

# Testen:
# Ändere den Wert von temperatur mehrmals manuell im Code (z. B. auf 30, 10 oder -2), um die Ausgaben zu prüfen.

# Lösung

temperatur=18

if temperatur >=25:
    print("Zieh ein T-Shirt an, es ist heiß!")
elif temperatur >=15:
    print("Ein Pullover reicht aus!")
elif temperatur >=5:
    print("Zieh dir eine warme Jacke an!")
else:
    print("Es ist eiskalt, zieh den Wintermantel an!")

# ==============================================================================

# Aufgabe 3: Das Fast-Food Menü (Medium)

# Erstelle ein Python-Programm für ein Bestellsystem im Fast-Food-Restaurant. 
# Der Kunde wählt ein Hauptgericht (Burger oder Wrap) und danach eine Beilage (Fritten oder Salat).

# Variablen definieren:
# Erstelle zwei Variablen:

        # - hauptgericht (ein Text, z. B. "Burger" oder "Wrap")

        # - beilage (ein Text, z. B. "Fritten" oder "Salat")

        # Bedingungen verschachteln:

# Nutze eine if-else-Struktur für das Hauptgericht. Innerhalb dieser Struktur prüfst du die Beilage:

        # - WENN das Hauptgericht "Burger" ist:

        # - Falls die Beilage "Fritten" ist: Ausgabe ➡ "Klassisches Burger-Menü mit Fritten wird zubereitet."

        # - Falls die Beilage "Salat" ist: Ausgabe ➡ "Fitness-Burger-Menü mit Salat wird zubereitet."

        # - Ansonsten: Ausgabe ➡ "Burger ohne gültige Beilage wird zubereitet."

        # - ANSONSTEN WENN das Hauptgericht "Wrap" ist:

        # - Falls die Beilage "Fritten" ist: Ausgabe ➡ "Wrap-Menü mit knusprigen Fritten wird zubereitet."

        # - Ansonsten: Ausgabe ➡ "Gesundes Wrap-Menü wird zubereitet."

        # - ANSONSTEN (weder Burger noch Wrap):

        # - Ausgabe ➡ "Dieses Hauptgericht steht nicht auf der Speisekarte."

# Testen:
# Ändere die Werte von hauptgericht und beilage manuell, um die Kombinationen zu testen.

# Lösung

hauptgericht="Pizza"
beilage="Fritten"

if hauptgericht=="Burger":
    if beilage=="Fritten":
        print("Klassisches Burger-Menü mit Fritten wird zubereitet!")
    elif beilage=="Salat":
        print("Fitness-Burger-Menü mit Salat wird zubereitet.")
    else:
        print("Burger ohne gültige Beilage wird zubereitet.")
elif hauptgericht=="Wrap":
    if beilage=="Fritten":
        print("Wrap-Menü mit knusprigen Fritten wird zubereitet.")
    else:
        print("Gesundes Wrap-Menü wird zubereitet.")
else:
    print("Dieses Hauptgericht steht nicht auf der Speisekarte.")
    
# ==============================================================================

# Aufgabe 4: Das Hotel-Buchungssystem (Schwer)

# Du programmierst ein Buchungssystem für ein Hotel. Der Preis hängt von der Zimmerart ab, ob der Gast Meerblick wünscht, und ob es einen Last-Minute-Rabatt gibt.

# Variablen definieren:
# Erstelle drei Variablen mit folgenden Startwerten:

        # - zimmerart (Text: "Einzelzimmer" oder "Doppelzimmer")

        # - meerblick (Boolescher Wert: True oder False)

        # - last_minute (Boolescher Wert: True oder False)

        # - gesamtpreis (Zahl, Startwert 0)

# Logik und Bedingungen umsetzen:
# Berechne den Preis Schritt für Schritt mit einer verschachtelten Struktur:

        # - Grundpreis bestimmen:

        # - Wenn die Zimmerart "Einzelzimmer" ist ➡ Grundpreis = 50 Euro.

        # - Wenn die Zimmerart "Doppelzimmer" ist ➡ Grundpreis = 80 Euro.

        # - Bei jeder anderen Eingabe ➡ Ausgabe: "Fehler: Diese Zimmerart existiert nicht!" (Programm soll den Preis dann nicht weiter berechnen).

        # - Extra berechnen (Verschachtelung):

        # - Innerhalb der jeweiligen Zimmerart kostet der Meerblick extra:

        # - Bei einem "Einzelzimmer" kostet der Meerblick + 10 Euro.

        # - Bei einem "Doppelzimmer" kostet der Meerblick + 20 Euro.

        # - Rabatt prüfen (Kombinierte Bedingung mit and):

        # - Wenn die Buchung Last Minute ist (last_minute == True) UND der aktuelle Preis über 65 Euro liegt, gibt es 15 Euro Rabatt auf den Gesamtpreis.

        # - Ansonsten gibt es keinen Rabatt.

# Aufgabe:
# Gib am Ende den finalen Buchungspreis sauber auf dem Bildschirm aus.

# Testen:
# Probiere verschiedene Kombinationen. Beispiel:

# zimmerart = "Doppelzimmer", meerblick = False, last_minute = True
# Ergebnis: 80 Euro - 15 Euro Rabatt = 65 Euro.

# Lösung 

# ==============================================================================
