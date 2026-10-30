# ==============================================================================

# input() -> Funktion in Python selbst. Muss nicht installiert werden.
# 1) Pausiert den Programmablauf 
# 2) Warte auf Tastatureingabe (Benutzer)
# 3) Enter-Taste -> Bestätigt
# WICHTIG: Die Funktion input() -> gibt STRING zurück!!

name = input("Wie heißt du? ")   # Was in der Klammer bei input() steht, wird in der Konsole angezeigt.
print("Hallo",name,"!")
# print("Hallo, " + name + "!")

alter = input("Wie alt bist du? ")
alter = int(alter)     # Konvertierung     Muss gemacht werden da es sonst ein String bleibt. Wenn ich dann etwas dazu rechnen möchte brauche ich aber einen integer.
print("Du bist " + str(alter) + " Jahre alt.")       # So sieht es in der Konsole besser aus die Antwort
nächstes_jahr = alter + 1
# print("Nächstes Jahr bist du " + str(nächstes_jahr) + " Jahre alt.")
print("Nächstes Jahr bist du",nächstes_jahr,"Jahre alt.")        # Geht beides

preis_netto = input("Was kostet 1 KG Kartoffeln? ")
# preis_netto = float(input("Was kostet 1 KG Kartoffeln? "))        # So kann man es auch schreiben
preis_brutto = float(preis_netto) * 1.07
print("Der Brutto-Preis beträgt:",preis_brutto,"Euro.")

antwort = input("Möchtest du fortfahren (ja/nein): ").lower()       # .lower -> Großgeschrieben wird automatisch klein konvertiert
if antwort == "ja":
    print("Super!")
elif antwort == "nein":
    print("Schade!")
else:
    print("Wie bitte??")

input("Drücke Enter zum beenden!")      # Letzer input damit man die Konsole noch lesen kann

# input("\nDrücke Enter zum beenden!")  # \n für ein Enter also untereinander schreiben

# ==============================================================================