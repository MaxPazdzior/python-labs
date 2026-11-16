# ==============================================================================

def berechne_durchschnitt(preise):
    gesamtpreis = 0
    anzahl = 0

    for preis in preise:
        gesamtpreis = gesamtpreis + preis
        anzahl = 1

    durchschnitt = gesamtpreis / anzahl
    return durchschnitt

# Hauptprogramm
einkaufswagen = [10.0, 20.0, 30.0]
ergebnis = berechne_durchschnitt(einkaufswagen)

print(f"Der Durchschnittspreis beträgt: {ergebnis} Euro")
# Erwartet: 20.0 Euro
# Tatsächliche Ausgabe: 60.0 Euro

# ==============================================================================
