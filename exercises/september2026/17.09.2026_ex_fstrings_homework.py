# ==============================================================================

# Aufgabe 01: Der Gepäckpreis-Rechner (f-String)
# Ein Fluganbieter berechnet den Preis für Gepäck nach Ticketklasse und Gewicht.

# Abfragen (input):
# - Ticketklasse: economy oder business?
# - Gewicht des Koffers (in kg, als ganze Zahl)?
 
# Bedingungen:
# - Economy: Bis zu 20 kg sind gratis. Jedes Kilo über 20 kg kostet 5.00 € extra.
# - Business: Bis zu 30 kg sind gratis. Jedes Kilo über 30 kg kostet 8.00 € extra.
 
# Ausgabe:
# Berechne die Zusatzkosten und gib sie auf zwei Nachkommastellen gerundet aus.
# Beispiel: "In der economy-Klasse kostet dein 25 kg Koffer 25.00 € extra."

# Lösung

ticket = input("Willkommen. Bitte gib deine Ticketklasse ein (economy/business)\n").lower()
gewicht = int(input("Nun gib bitte das Gewicht deinen Koffers in KG an.\n"))
extra_kosten = 0.0

if ticket == "economy":
    if gewicht > 20:
        extra_kosten = (gewicht - 20) * 5.0
elif ticket == "business":
    if gewicht > 30:
        extra_kosten = (gewicht - 30) * 8.0

print(f"In der {ticket}-Klasse kostet dein {gewicht}KG Koffer {extra_kosten:.2f}€ extra.")

# ==============================================================================

# Aufgabe 02: Der Stromtarif-Rechner (f-String)
# Ein Energieversorger berechnet den monatlichen Strompreis basierend auf dem Tarifmodell und dem Verbrauch.
 
# Abfragen:
# - Tarifmodell: basis oder oeko?
# - Stromverbrauch im Monat (in kWh, als ganze Zahl)?

# Bedingungen:
#   - Basis: Grundgebühr: 10.00 € pro Monat. Preis pro kWh: 0,30 €.
#   - Öko: Grundgebühr: 15.00 € pro Monat. Preis pro kWh: 0,25 €.

# Ausgabe:
# Berechne die monatlichen Gesamtkosten (Grundgebühr + Verbrauch * kWh-Preis).
# Gib das Ergebnis gerundet auf zwei Nachkommastellen aus.
# Beispiel: "Im oeko-Tarif zahlst du bei 200 kWh monatlich 65.00 €."

# Lösung

tarifmodell = input("Willkommen. Bitte gib dein Tarifmodell an (basis/öko)\n").lower()
stromverbrauch = int(input("Bitte gib nun deinen Stromverbrauch in kwh im Monat an.\n"))
gesamtkosten = 0.0

if tarifmodell == "basis":
    grundgebühr = 10.00
    kwh_preis = 0.30
    gesamtkosten = (grundgebühr + stromverbrauch * kwh_preis)
elif tarifmodell == "öko":
    grundgebühr = 15.00
    kwh_preis = 0.25
    gesamtkosten = (grundgebühr + stromverbrauch * kwh_preis)

print(f"Im {tarifmodell}-Tarif zahlst du bei {stromverbrauch}kwh monatlich {gesamtkosten:.2f}€")

# ==============================================================================
