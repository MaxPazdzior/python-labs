# ==============================================================================

# Aufgabe 01: Der smarte Rabatt-Rechner (f-String)
 
# Ein Online-Shop vergibt Rabatte basierend auf dem Bestellwert und dem Kundenstatus. 
# Frage zuerst den Bestellwert ab. Frage danach, ob der Kunde ein Premium-Mitglied ist (Antwort mit ja oder nein).
 
    # - Standard-Kunden erhalten ab 100 € Bestellwert 10 % Rabatt.
    # - Premium-Kunden erhalten generell 15 % Rabatt.
    # - Wenn der Bestellwert über 100 € liegt, erhalten sie sogar 20 % Rabatt.
 
# Berechne den finalen Rechnungsbetrag und wie viel Geld gespart wurde.
# Runde den Betrag im f-string auf genau zwei Nachkommastellen.
 
# Beispiel: "Dein finaler Preis ist 80.00 €. Du hast 20.00 € gespart!"

# Lösung

bestellwert = float(input("Wie hoch ist der Bestellwert? "))
ist_premium = input("Bist du Premium Mitglied? (ja/nein) ").lower()     # lower hinter dem input sorgt dafür, dass egal was der Benutzer eingibt, es kleingeschrieben wird

if ist_premium == "ja":
    if bestellwert >= 100:
        rabatt_satz = 0.20  # 20%
    else:
        rabatt_satz = 0.15
else:
    if bestellwert >= 100:
        rabatt_satz = 0.10
    else:
        rabatt_satz = 0.00

gespart = bestellwert * rabatt_satz
endpreis = bestellwert - gespart

print(f"Dein Finaler Preis ist: {endpreis:.2f}€. Du hast {gespart:.2f}€ gespart!")

# ==============================================================================