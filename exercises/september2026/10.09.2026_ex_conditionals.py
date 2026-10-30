# ==============================================================================

# Aufgabe 1
# Der Temperatur-Check
# Erstelle eine Variable temperatur und weise ihr direkt einen Zahlenwert zu (z.B.22).
# Das Programm muss dann folgendes ausgeben:

# Über 30(°C): "Es ist heiß!"
# 15 bis 30: "Angenehm."
# 0 bis 14: "Zieh eine Jacke an."
# Unter 0: "Frostig!"


# Meine Lösung

temperatur = 31

if temperatur > 30:
    print("Es ist heiß!")
elif temperatur >=15 and temperatur <=30:
    print("Angenehm.")
elif temperatur >=0 and temperatur <=14:
    print("Ziehe eine Jacke an.")
elif temperatur <0:
    print("Frostig!")

# Daniels Lösung

temperatur = 31

if temperatur > 30:
    print("Es ist heiß!")
elif temperatur >= 15:
    print("Angenehm.")
elif temperatur >= 0:
    print("Zieh eine Jacke an.")
else:
    print("Frostig!")

# ==============================================================================

# Aufgabe 2
# Der Snack-Check
# Stellen Sie sich vor, Sie programmieren eine Logik für ein Qualitätskontrollsystem.
# Es soll prüfen, ob ein Apfel verzehrbar ist. Dafür gibt es zwei Kriterien: Ob er reif ist und ob er faul ist.
# Erstellen Sie zwei Variablen: ist reif = True und ist faul = False.
# Prüfen Sie zuerst: Ist der Apfel reif?
# Falls dies zutrifft, prüfen Sie innerhalb dieser Bedingung: Ist der Apfel faul?
# Falls er faul ist: Geben Sie „Wegwerfen!" aus.
# Falls er nicht faul ist: Geben Sie „Guten Appetit!" aus.
# Falls der Apfel noch nicht reif ist: Geben Sie „Warten..." aus.


# Meine Lösung (Ist falsch, da das untere else zum ersten if soll)

apfel_ist_reif = TRUE
apfel_ist_faul = FALSE

if apfel_ist_reif:
    if apfel_ist_faul:
        print("Wegwerfen!")
    elif apfel_ist_reif:
        print("Guten Appetit!")
    else:
        print("Warten...")


# Daniels Lösung

ist_reif = False
ist_faul = True

if ist_reif:
    if ist_faul:
        print("Wegwerfen!")
    else:
        print("Guten Appetit!")
else:
    print("Warten...")

# ==============================================================================
