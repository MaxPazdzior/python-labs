# ==============================================================================

# Hausaufgabe 01: Statistik-Rechner
 
# 1. Schreibe eine Funktion namens berechne_statistik(zahlen_liste).

# 2. Die Funktion soll eine Liste von Zahlen entgegennehmen und drei Werte berechnen:
# 	• Die Summe aller Zahlen.
# 	• Die Anzahl der Zahlen.
# 	• Den Durchschnitt (Mittelwert) der Zahlen.

# 3. Die Funktion soll diese drei Ergebnisse als ein einziges Tupel zurückgeben (return).

# 4. Erstelle außerhalb der Funktion eine Test-Liste (z. B. mit den Zahlen [10, 20, 30, 40]), 
# rufe die Funktion damit auf und entpacke das zurückgegebene Tupel in drei Variablen, um das Ergebnis sauber auszudrucken.

# Lösung

def berechne_statistik(zahlen_liste):
    summe = sum(zahlen_liste)
    anzahl = len(zahlen_liste)
    durchschnitt = summe / anzahl
    return summe, anzahl, durchschnitt

zahlen_liste = [10,20,30,40]
summe, anzahl, durchschnitt = berechne_statistik(zahlen_liste)
print(f"Die Werte sind: ", berechne_statistik(zahlen_liste))
print(f"\nDie Summe aller Zahlen ist: {summe}\nDie Anzahl der Zahlen in der Liste ist: {anzahl}\nDer Durchschnitt aller Zahlen in der Liste ist: {durchschnitt}")

# ==============================================================================

# Hausaufgabe 02: Ein Gaming-Leaderboard
 
# In einem Multiplayer-Spiel werden die besten Spieler in einer Liste von Tupeln gespeichert. 
# Jedes Tupel enthält die Daten im Format (Spielername, Level, Score):
# leaderboard = [("CyberKnight", 45, 12500), ("PixelQueen", 50, 15200), ("ShadowGamer", 32, 8900), ("NoobMaster", 12, 1500)]

# 1. Schreibe eine for-Schleife, die das Leaderboard durchläuft und alle Spieler ausgibt, 
# die bereits Level 40 oder höher erreicht haben.

# 2. Berechne den durchschnittlichen Score aller Spieler auf dem Leaderboard.
 
# Gegebene Datenstruktur: Liste von Tupeln (Name, Level, Score)
leaderboard = [
    ("CyberKnight", 45, 12500), 
    ("PixelQueen", 50, 15200), 
    ("ShadowGamer", 32, 8900), 
    ("NoobMaster", 12, 1500)
]

# Lösung

spielernamen = []
score_sammler = []

leaderboard = [
     ("CyberKnight", 45, 12500), 
     ("PixelQueen", 50, 15200), 
     ("ShadowGamer", 32, 8900), 
     ("NoobMaster", 12, 1500)
]

for namen, level, score in leaderboard:
    if level >=40:
        spielernamen.append(namen)
    score_sammler.append(score)

durchschnitt = sum(score_sammler) / len(score_sammler)

    
print(f"Die Namen aller Spieler mit Level 40 oder höher sind: {spielernamen}")
print(f"\nDer Durchschnittsscore aller Spieler ist: {durchschnitt}")

# ==============================================================================

# Hausaufgabe 03: Wetterstationsnetzwerk

# Ein Wetterdienst verwaltet seine Messstationen in einem Dictionary. 
# Als Schlüssel wird ein Tupel (breitengrad, laengengrad) genutzt, der Wert (Value) ist die dort gemessene Temperatur.

# 1. Erstelle ein Dictionary namens wetter_daten mit drei bekannten Stationen:
# 	• (52.5, 13.4) (Berlin) → 18.5
# 	• (48.1, 11.5) (München) → 21.0
# 	• (53.5, 10.0) (Hamburg) → 14.2

# 2. Schreibe eine Funktion namens wetter_check(datenbank, lat, lon). 
# Die Funktion hat die Datenbank und die zwei Koordinaten als Parameter.

# 3. Die Funktion soll folgendes tun:
# 	• Prüfen, ob das Koordinaten-Tupel (lat, lon) bereits im Dictionary existiert.
# 	• Wenn die Station existiert, soll sie die gespeicherte Temperatur ausgeben: "Station bekannt. Temperatur: X °C."
# 	• Wenn die Station nicht existiert, soll sie die Koordinaten neu hinzufügen. 
# Da noch keine Messung vorliegt, soll die Temperatur fest im Code auf den Standardwert 0.0 gesetzt werden. 
# Ausgabe: "Neue Station registriert. Start-Temperatur auf 0.0 °C gesetzt."

# 4. Teste die Funktion mit einer bekannten Station und danach mit einer neuen Station.

# Lösung

wetter_daten = {
    (52.5,13.4): {"Temperatur": 18.5},
    (48.1,11.5): {"Temperatur": 21.0},
    (53.5,10.0): {"Temperatur": 14.2}
}

def wetter_check(datenbank, lat, lon):
    koordinate = (lat, lon)
    if koordinate in datenbank:
        print(f"Station bekannt. Temperatur: {datenbank[koordinate]["Temperatur"]} °C")
    else:
        datenbank[koordinate]={"Temperatur": 0.0}
        print("Neue Station registriert. Start-Temperatur auf 0.0 °C gesetzt.")            

wetter_check(wetter_daten, 52.5,13.5)
print(wetter_daten)

# ==============================================================================

# Hausaufgabe 04: Bigrams aufzählen (Schwer!)
 
# In der Textanalyse werden Texte oft in sogenannte Bigrams (Zweier-Wortpaare) zerlegt, 
# um den Schreibstil oder die Häufigkeit von Phrasen zu untersuchen. 
# Ein Bigram wird in Python perfekt als Tupel aus zwei Strings dargestellt: ("wort1", "wort2").

# 1. Gegeben ist ein Text (als String):
# text = "künstliche intelligenz basiert auf daten und künstliche intelligenz nutzt maschinelles lernen weil 
# maschinelles lernen die zukunft ist"

# 2. Schreibe eine Funktion namens generiere_haeufige_bigrame(text_string, mindesthaeufigkeit).

# 3. Die Funktion muss Folgendes tun:
# 	• Den Text in Kleingebuchstaben umwandeln und in eine Liste einzelner Wörter splitten.
# 	• Aus der Wortliste alle aufeinanderfolgenden Paare als Tupel generieren 
#     (Beispiel: aus ["python", "ist", "super"] werden die Tupel ("python", "ist") und ("ist", "super")).
# 	• Die Häufigkeit jedes Bigram-Tupels in einem Dictionary zählen (das Tupel ist der Key, die Anzahl der Value).
# 	• Alle Bigrame herausfiltern, die seltener als die mindesthaeufigkeit vorkommen.
# 4. Die Funktion soll eine Liste von verschachtelten Tupeln im Format [((w1, w2), anzahl), ...] zurückgeben.

# 5. Teste die Funktion mit dem gegebenen Text und einer Mindesthaeufigkeit von 2.

# Lösung

text = "künstliche intelligenz basiert auf daten und künstliche intelligenz nutzt maschinelles lernen weil maschinelles lernen die zukunft ist"

def generiere_haeufige_bigrame(text_string, mindesthaeufigkeit):


# ==============================================================================
