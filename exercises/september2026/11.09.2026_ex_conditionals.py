# ==============================================================================

# Aufgabe 1: Kleidungsempfehlung
# Schreibe ein Python-Programm, das eine Temperatur in Grad Celsius überprüft und dem Nutzer eine passende Kleidungsempfehlung ausgibt. 
# Definiere dafür zuerst eine Variable für die Temperatur und weise ihr einen beliebigen Wert zu.
# Wenn die Temperatur unter null Grad liegt, soll das Programm den Hinweis ausgeben, 
# dass man eine dicke Winterjacke anziehen soll. 
# Liegt der Wert hingegen im Bereich von null bis einschließlich fünfzehn Grad, 
# wird die Nachricht ausgegeben, dass ein warmer Pullover reicht.
# Für mildere Temperaturen bis einschließlich fünfundzwanzig Grad soll die Rückmeldung erscheinen, 
# dass ein T-Shirt und eine leichte Jacke perfekt sind. 
# In allen anderen Fällen, also bei Temperaturen über fünfundzwanzig Grad, gibt das Programm schließlich aus, 
# dass es heiß ist und
# T-Shirt sowie Shorts ausreichen.

# Meine Lösung: (Kann man so machen muss man aber nicht da es zu viel ist.)

temperatur = 8

if temperatur <0:
    print("Ziehe eine dicke Winterjacke an!")
elif temperatur >=0 and temperatur <=15:
    print("Ein warmer Pullover reicht heute.")
elif temperatur >=16 and temperatur <=25:
    print("Ein T-Shirt und eine leichte Jacke sind heute perfekt.")
elif temperatur >25:
    print("Es ist zu heiß. Ein T-Shirt und Shorts reichen heute aus.")

# Daniels Lösung:

temperatur = 15

if  temperatur < 0:
    print("Zieh eine dicke Winderjacke an!")
elif temperatur <= 15:
    print("Ein warmer Pullover reicht.")
elif temperatur <= 25:
    print("Ein T-Shirt und eine leichte Jacke.")
else:
    print("Es ist heiß! T-Shirt und Shorts reichen.")

# ==============================================================================

# Aufgabe 2: Notenauswertung über Variablen

# Erstelle ein Python-Programm, das eine vordefinierte Punktzahl auswertet und das entsprechende Feedback auf dem Bildschirm ausgibt.

# 1. Variable definieren:
#    Erstelle eine Variable namens punkte und weise ihr einen ganzzahligen Wert zu (z. B. 90).

# 2. Bedingungen prüfen:
#    Nutze eine if-elif-else-Struktur, um den Wert der Variable nach folgenden Regeln zu prüfen:

#    - Ab 90 Punkten: "Sehr gut!"
#    - Ab 80 Punkten: "Gut!"
#    - Ab 70 Punkten: "Befriedigend."
#    - Ab 60 Punkten: "Ausreichend."
#    - Unter 60 Punkten: "Leider nicht bestanden!"

# 3. Testen:
#    Ändere den Wert der Variable punkte mehrmals manuell im Code, um zu prüfen, ob alle Textausgaben korrekt funktionieren

# Meine Lösung: (Daniel hat die selbe Lösung)

punkte = 59

if punkte >=90:
    print("Sehr gut!")
elif punkte >=80:
    print("Gut!")
elif punkte >=70:
    print("Befriedigend!")
elif punkte >=60:
    print("Ausreichend!")
else:
    print("Leider nicht bestanden!")

# ==============================================================================

# Aufgabe 3: Eintrittspreise berechnen
# Ein Zoo berechnet die Eintrittspreise automatisch basierend auf dem Alter des Besuchers und der 
# Frage, ob die Person ein Student ist.
#     1. Variablen vorgeben: Erstelle zwei Variablen mit festen Werten:
#         ◦ alter = 22 (Das Alter des Besuchers als Zahl)
#         ◦ ist_student = True (Ein Boolean-Wert, der angibt, ob die Person studiert)
#     2. Logische Prufung (if-elif-else): Bestimme den Ticketpreis nach folgenden Regeln:
#         ◦ Kinder unter 4 Jahren zahlen nichts (0 Euro).
#         ◦ Kinder und Jugendliche von 4 bis 17 Jahren zahlen 8 Euro.
#         ◦ Erwachsene (ab 18 Jahren):
#             ▪ Wenn die Person Student ist, zahlt sie einen ermaßigten Preis von 12 Euro.
#             ▪ Wenn die Person kein Student ist, zahlt sie den vollen Preis von 15 Euro.
#         ◦ Senioren (ab 65 Jahren) erhalten einen Spezialpreis von 10 Euro (egal ob Student oder nicht).
#     3. Gib den berechneten Ticketpreis auf dem Bildschirm aus (z. B. "Der Ticketpreis betragt 12 Euro").

# Meine Lösung:

alter = 35
ist_student = False

if alter <4:
    print("Der Eintritt ist frei viel Spaß!")
elif alter <=17:
    print("Willkommen Sie müssen 8€ zahlen!")
elif alter >=65:
    print("Seniorenrabatt angewendet. Sie müssen 10€ zahlen!")
else:
    if alter >=18 and ist_student:
        print("Studenten Rabatt angewand. Sie zahlen nur 12€")
    else:
        print("Der Preis beträgt 15€")

# ==============================================================================
