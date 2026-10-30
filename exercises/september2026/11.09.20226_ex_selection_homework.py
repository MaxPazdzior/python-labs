# ==============================================================================

# Aufgabe 1: Der Versandkosten-Rechner

# Erstelle ein Python-Programm, das den Bestellwert eines Kunden prüft und die dazugehörigen Versandkosten sowie den Gesamtbetrag 
# auf dem Bildschirm ausgibt.

# Variable definieren:
# Erstelle eine Variable namens bestellwert und weise ihr einen Wert zu (z. B. 45).

# Bedingungen prüfen:
# Nutze eine if-elif-else-Struktur, um die Versandkosten nach folgenden Regeln zu ermitteln:

#       - Ab 100 Euro: Der Versand ist kostenlos (0 Euro).
#       - Ab 50 Euro: Die Versandkosten betragen 2 Euro.
#       - Ab 20 Euro: Die Versandkosten betragen 4 Euro.
#       - Unter 20 Euro: Die Versandkosten betragen 6 Euro.

# Ausgabe berechnen:
# Das Programm soll am Ende zwei Dinge auf dem Bildschirm ausgeben:

#       - Wie hoch die Versandkosten sind.
#       - Wie hoch der Gesamtbetrag (Bestellwert + Versandkosten) ist.

# Testen:
# Ändere den bestellwert mehrmals manuell im Code (z. B. auf 120, 60 oder 15), um zu prüfen, ob das Programm immer richtig rechnet.

# Lösung

bestellwert = 20.99 # In Euro
versandkosten = 0   # In Euro

if bestellwert >=100:
    versandkosten=0
    print("Bestellwert:", bestellwert, "Versankosten:", versandkosten, "Summe:", bestellwert+versandkosten)
elif bestellwert >=50:
    versandkosten=2
    print("Bestellwert:", bestellwert, "Versankosten:", versandkosten, "Summe:", bestellwert+versandkosten)
elif bestellwert >=20:
    versandkosten=4
    print("Bestellwert:", bestellwert, "Versankosten:", versandkosten, "Summe:", bestellwert+versandkosten)
else:
    versandkosten=8
    print("Bestellwert:", bestellwert, "Versankosten:", versandkosten, "Summe:", bestellwert+versandkosten)

# ==============================================================================

# Aufgabe 2: Der Ei-Koch-Timer

# Erstelle ein Python-Programm, das eine Kochzeit in Minuten auswertet und ausgibt, wie das Ei nach dieser Zeit gekocht ist.

# Variable definieren:
# Erstelle eine Variable namens kochzeit und weise ihr einen ganzzahligen Wert zu (z. B. 6 für 6 Minuten).

# Bedingungen prüfen:
# Nutze eine if-elif-else-Struktur, um das Ei nach folgenden Regeln zu bewerten:

# - Ab 10 Minuten: "Das Ei ist steinhart gekocht."
# - Ab 7 Minuten: "Das Ei ist hart, das Eigelb ist fest."
# - Ab 5 Minuten: "Das perfekte Wachsei!"
# - Ab 3 Minuten: "Das Ei ist sehr weich, das Eiweiß ist gerade so fest."
# - Unter 3 Minuten: "Das Ei ist noch fast roh!"

# Testen:
# Ändere den Wert von kochzeit mehrmals manuell im Code (z. B. auf 2, 5 oder 12), um zu prüfen, ob der richtige

# Lösung:

kochzeit = 2   # In Minuten

if kochzeit >=10:
    print("Das Ei ist steinhart gekocht.")
elif kochzeit >=7:
    print("Das Ei ist hart, das Eigelb ist fest.")
elif kochzeit >=5:
    print("Das perfekte Wachsei!")
elif kochzeit >=3:
    print("Das Ei ist sehr weich , das Eiweiß ist gerade so fest.")
else:
    print("Das Ei ist noch fast Roh")

# ==============================================================================

# Aufgabe 3: Der smarte Kaffeeautomat

# Erstelle ein Python-Programm für einen Kaffeeautomaten. Der Automat bietet zwei Getränkearten an (Kaffee oder Tee). Je nachdem, was gewählt wurde, fragt der Automat nach einer zweiten Option (Milch oder Zucker).

# Variablen definieren:
# Erstelle zwei Variablen:

# - getraenk (ein Text, z. B. "Kaffee" oder "Tee")
# - extra (ein Text, z. B. "Milch", "Zucker" oder "keines")

# Bedingungen verschachteln:
# Nutze eine if-else-Struktur für das Getränk. Innerhalb dieser Struktur prüfst du das Extra:

# - WENN das Getränk "Kaffee" ist:
#   - Falls das Extra "Milch" ist: Ausgabe ➡ "Kaffee mit Milch wird zubereitet."
#   - Falls das Extra "Zucker" ist: Ausgabe ➡ "Süßer Kaffee wird zubereitet."
#   - Ansonsten: Ausgabe ➡ "Schwarzer Kaffee wird zubereitet."

# - ANSONSTEN WENN das Getränk "Tee" ist:
#   - Falls das Extra "Zucker" ist: Ausgabe ➡ "Süßer Tee wird zubereitet."
#   - Ansonsten: Ausgabe ➡ "Reiner Tee wird zubereitet."

# - ANSONSTEN (weder Kaffee noch Tee):
#   - Ausgabe ➡ "Dieses Getränk ist leider nicht verfügbar."

# Testen:
# Ändere die Werte von getraenk und extra manuell im Code, um zu sehen, ob der Automat jede Kombination richtig versteht (z. B. Kaffee mit Milch, Tee mit Zucker oder Cola).

# Lösung

getränk="Kaffee"
extra="Zucker"

print("Getränk:", getränk)
print("Extra:", extra)

if getränk=="Kaffee":
    if getränk=="Kaffee" and extra=="Milch":
        print("Kaffee wird mit Milch zubereitet.")
    elif getränk=="Kaffee" and extra=="Zucker":
        print("Süßer Kaffee wird zubereitet.")
    else:
        print("Schwarzer Kaffee wird zubereitet.")
elif getränk=="Tee":
    if getränk=="Tee" and extra=="Zucker":
        print("Süßer Tee wird zubereitet.")
    else:
        print("Reiner Tee wird zubereitet.")
else:
    print("Dieses Getränk ist leider nicht verfügbar.")

# ==============================================================================

# Aufgabe 4: Der smarte Pizza-Lieferdienst

# Du programmierst das Bestellsystem für eine Pizzeria. Das Programm soll den Endpreis für eine Bestellung berechnen. 
# Der Preis hängt von der Pizzagröße, einem Extra-Wunsch (Käserand) und einem Rabatt für Selbstabholer ab.

# Variablen definieren:
# Erstelle drei Variablen mit folgenden Startwerten:

#       - groesse (Text: "Standard" oder "Family")
#       - kaesrand (Boolescher Wert: True oder False)
#       - abholung (Boolescher Wert: True oder False)

# Logik und Bedingungen umsetzen:
# Berechne den Preis Schritt für Schritt mit einer verschachtelten Struktur:

# - Grundpreis bestimmen:
#           - Wenn die Größe "Standard" ist ➡ Grundpreis = 9 Euro.
#           - Wenn die Größe "Family" ist ➡ Grundpreis = 15 Euro.
#           - Bei jeder anderen Eingabe ➡ Ausgabe: "Fehler: Diese Größe gibt es nicht!" (Das Programm sollte dann nicht weiterrechnen.)

# - Extra berechnen (Verschachtelung):
#       - Innerhalb der jeweiligen Pizzagröße kostet der Käserand extra:
#       - Bei einer "Standard"-Pizza kostet der Käserand + 2 Euro.
#       - Bei einer "Family"-Pizza kostet der Käserand + 4 Euro.

# - Rabatt prüfen (Kombinierte Bedingung):
#       - Wenn der Kunde die Pizza selbst abholt (abholung == True) und der aktuelle Preis über 12 Euro liegt, bekommt er 3 Euro Rabatt auf den Gesamtpreis.
#       - Ansonsten gibt es keinen Rabatt.

# Aufgabe:
# Gib den finalen Gesamtpreis sauber auf dem Bildschirm aus.

# Testen:
# Probiere folgende Kombinationen aus, um zu sehen, ob dein Programm fehlerfrei rechnet:

#   - groesse = "Standard", kaeserand = False, abholung = True
#   - Ergebnis: 9 Euro, da Preis nicht über 12 Euro liegt

#   - groesse = "Family", kaeserand = True, abholung = True
#   - Ergebnis: 16 Euro: 15 + 4 - 3 Rabatt

# Lösung

größe="Family"
käserand=False
abholung=False
grundpreis=0

if größe=="Standard":
    grundpreis=9
    if käserand:
        grundpreis+=2
elif größe=="Family":
    grundpreis=15
    if käserand:
        grundpreis+=4
else:
    print("Diese Pizzagröße gibt es nicht!")

if abholung and größe=="Standard" and grundpreis>12:
    grundpreis-=3
    print("Summe:", grundpreis)
elif abholung and größe=="Family" and grundpreis>12:
    grundpreis-=3
    print("Summe:", grundpreis)
else:
    print("Summe:", grundpreis)

# ==============================================================================
