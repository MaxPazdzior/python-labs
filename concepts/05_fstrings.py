# ==============================================================================

# f-String "formatted string"
# Python 3.6

name = "Alice"
alter = 30

print("Hallo",name,"! Du bist",alter,"Jahre alt.")      # So sieht es nicht gut aus weil zwischen dem "!" Leerzeichen sind
print(f"Hallo {name}! Du bist {alter} Jahre alt.")      # Das ist ein fstring
print(f"Nächstes Jahr wirst du {alter+1} sein.")

x = 10
y = 5
print(f"Summe: {x+y}, Produkt: {x*y}")

pi = 3.1415926
print(f"Pi gerundet: {pi:.2f}")     # Punkt hinter Pi = Komma in Python -> 2 = 2 Stellen nach dem Komma (gerundet) -> f = Float

a = 4.123
b = 1.4
c = 100.99999

print("A ->",a)
print("B ->",b)
print("C ->",c)

print(f"A -> {a:8.2f}")     # 8 nach dem Doppelpunkt = Reserviert 8 Zeichen in der Konsole für die Ausgabe
print(f"B -> {b:8.2f}")     # Würde man eine Zahl vor der 8 schreiben als Beispiel 0 werden die Leerzeichen durch 0 ersetzt
print(f"C -> {c:8.2f}")

# Prozent
fortschritt = 0.751643      # Zahlen die mit 0 Anfangen kann man als Prozent ausgeben
print(f"Fortschritt: {fortschritt:.1%}")        # So würde man Prozent anzeigen lassen

# Debugging
user = "admin"
wert = 41.7
print(f"{user=}:{wert=}")       # = Zeigt an, welche Variablen zugewiesen wurden. Gut für Fehlersuche

text = "hallo"
print(f"{text:>50}")        # > Bedeutet, dass die Ausgabe rechtsbündig ist
print(f"{text:^50}")        # ^ Lässt den Text mittig anzeigen

geld = 10000000000
print(f"{geld:,}")      # , Bedeutet, dass die Zahl richtig geschrieben wird mit Trennung in der Konsole (10,000,000,000)

# ==============================================================================