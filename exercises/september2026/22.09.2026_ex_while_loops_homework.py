# ==============================================================================

# Das Kino-Ticketsystem
 
# Schreibe ein Programm für ein kleines Kino mit 20 freien Sitzplätzen. Das Programm verkauft Tickets, bis das Kino voll ist.

# Die Regeln:
#   1) Die Schleife läuft so lange, wie Plätze frei sind.
#   2) Der Benutzer wird gefragt, wie viele Tickets er kaufen möchte.
#   3) Wenn die Eingabe kleiner oder gleich 0 ist, zeige: "Ungültige Ticketanzahl!".
#   4) Wenn der Benutzer mehr Tickets kaufen möchte, als noch Plätze frei sind,
#   zeige: "So viele freie Plätze haben wir nicht mehr!" und nenne die Anzahl der Restplätze.
#   5) Wenn genügend Plätze da sind, ziehe die Tickets von den freien Plätzen ab und bestätige den Kauf.
#   6) Am Ende (wenn das Kino voll ist) gibt das Programm aus: "Ausverkauft! Der Kinosaal ist voll."

# Lösung

summe = 20

while True:
    eingabe = int(input("Bitte geben Sie an, wie viele Tickets Sie kaufen möchten.\n"))
    
    if eingabe <= 0:
        print("Ungültige Ticketanzahl! Versuchen Sie es noch einmal!")
    elif eingabe <= summe:
        summe -= eingabe
        print("Dein Kauf war erfolgreich!")
        
        if summe == 0:
            print("Ausverkauft! Der Kinosaal ist nun voll!")
            break
    else:
        print(f"So viele Sitze haben wir nicht mehr. Wir haben noch {summe} freie Sitze!")



# ============================================================================== 

# Der Sicherheits-Bankautomat
 
# Schreibe ein Programm, das ein PIN-Eingabesystem und ein einfaches Terminal-Kontomenü simuliert. Der Benutzer hat maximal drei Versuche, die richtige PIN einzugeben. 
# War die Eingabe erfolgreich, öffnet sich ein Menü im Terminal für Kontoverzweigungen.
 
# Regeln für den Automaten:
#     1. PIN-Sperre: Die richtige PIN lautet 1234. Der Benutzer hat 3 Versuche. Nutze eine Variable als Zähler.
#     2. Schleife: Läuft die PIN-Prüfung schief, wird ein Versuch abgezogen. Nach 3 Fehlversuchen bricht das Programm ab.
#     3. Hauptmenü: Bei korrekter PIN startet eine neue Endlosschleife while True. Setze den Startkontostand auf 500 Euro.
#     4. Befehle im Menü:
#         ◦ kontostand: Zeigt das aktuelle Guthaben per f-string an.
#         ◦ einzahlen: Fragt nach einem Betrag (als String über input), wandelt ihn in eine Zahl um und rechnet ihn auf das Guthaben an.
#         ◦ auszahlen: Fragt nach einem Betrag. Prüfe mit if, ob genug Geld da ist. Wenn ja, ziehe es ab. Wenn nein, zeige eine Fehlermeldung.
#         ◦ ende: Verabschiedet den Benutzer und beendet das Programm (break).
#         ◦ Jede andere Eingabe gibt eine Fehlermeldung aus.

# Lösung

versuche = 3
programm_aktiv = True

while versuche > 0 and programm_aktiv:
    pin = input("Willkommen. Bitte geben Sie nun Ihren Pin ein:\n")

    if pin == "1234":
        print("Login Erfolgreich!")
        guthaben = 500

        while True:
            eingabe = input("\nBitte geben Sie nun einen Befehl ein (kontostand, einzahlen, auszahlen, ende).\n")

            if eingabe == "kontostand":
                print(f"Ihr Guthaben beträgt {guthaben}€.")

            elif eingabe == "einzahlen":
                betrag_text = input("Geben Sie nun Ihren Betrag ein!\n")
                if betrag_text.isnumeric():
                    betrag = int(betrag_text)
                    guthaben += betrag
                    print(f"Ihr Guthaben wurde erfolgreich aufgeladen. Neues Guthaben: {guthaben}€")
                else:
                    print("Ungültige Eingabe. Geben Sie eine Zahl an.")

            elif eingabe == "auszahlen":
                betrag_text = input("Bitte geben Sie ein, wie viel Geld abgebucht werden soll:\n")
                if betrag_text.isnumeric():
                    betrag = int(betrag_text)
                    if betrag <= guthaben:
                        guthaben -= betrag
                        print(f"Abbuchung erfolgreich! Ihr neues Guthaben beträgt nun {guthaben}€")
                    else:
                        print(f"Fehler! Nicht genügend Guthaben vorhanden. Ihr Kontostand beträgt {guthaben}€.")
                else:
                    print("Ungültige Eingabe. Geben Sie eine Zahl an.")

            elif eingabe == "ende":
                print("Beehren Sie uns bald wieder!")
                programm_aktiv = False 
                break

            else:
                print(f"Fehler! Die Eingabe '{eingabe}' unterstützen wir nicht!")

    else:
        versuche -= 1
        if versuche == 0:
            print("Sie haben den Pin 3x falsch eingegeben. Aus Sicherheitsgründen wurde Ihr Konto gesperrt!")
        else:
            print(f"Der Pin ist falsch, Sie haben noch {versuche} Versuche!")

 
# ==============================================================================
