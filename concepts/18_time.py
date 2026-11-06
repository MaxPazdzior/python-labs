# ==============================================================================

import time
import random

# ==============================================================================

# Modul time: Sehr Maschinennah, einfachen Unix-Zeitstempel
# Ideal für: Messungen von Code-Laufzeiten, künstliche Pausen im Code

# ==============================================================================

# 1) Programm pausieren mit time.sleep()

def countdown(sekunden):
    print("Countdown startet...")
    for i in range(sekunden, 0, -1):    # -1 damit es runter zählt und 0 damit es bei 0 aufhört
        print(f"Noch {i} Sekunden...", end="\r")    # --> Mit end="\r" wird es in der Konsole überschrieben anstatt alles in der Konsole anzuzeigen. Carriage return
        time.sleep(1)   # --> Hier wird eine Sekunde gewartet, bis das nöchste Ergebnis in der Konsole erscheint (Pause gemacht) 
    print("Zeit abgelaufen!")

# countdown(5)

def draw_art(size):
    for i in range(size):
        zeichen = random.choice(["^","°"])  # --> Hier wird ein Random Zeichen generiert von den beiden
        print(zeichen, end="", flush=True)  # --> end="" bedeutet, er schreibt die Zeichen nebeneinander. Ohne flush würde Python das Ergebnis nicht im Termin anzeigen
        time.sleep(0.1)

# draw_art(30)

# ==============================================================================

# 2) Laufzeit messen mit time.perf_counter()

start_zeit = time.perf_counter()    # --> Hier startet der Timer

# print("Code wird ausgeführt...")
time.sleep(1)

end_zeit = time.perf_counter()  # --> Hier endet der Timer
laufzeit = end_zeit - start_zeit    # --> Hier berechnen wir die gesammte Laufzeit
# print(f"Das Programm hat {laufzeit} Sekunden gebraucht.")

# ==============================================================================

# Aufgabe: Listen vs. Sets

groesse = 10_000_000    # --> Man kann Zahlen auch so trennen für die Übersicht. Im Terminal wird es ohne die Striche angezeigt
daten_liste = list(range(groesse))  # --> Hier wird die Größe gesplittet und in die Liste gespeichert. Also alle 10 Miliionen Zahlen
daten_set = set(daten_liste)    # --> Hier wird es anstatt in einer Liste in ein Set gespeichert

such_element = 9_999_999    # --> Das benutzen wir um zu schauen, wie lange es braucht bis die Liste und das Set diese Zahl findet

print("Suche startet...")

# Messung 1 Liste
start_liste = time.perf_counter() # --> Hier wird der Timer für die Liste gestartet
gefunden = such_element in daten_liste
end_liste = time.perf_counter() # --> Hier wird das Ende gespeichert
zeit_liste = end_liste - start_liste
print(f"Liste: {zeit_liste:.6f} Sekunden")

# Messung 2 Set
start_set = time.perf_counter()
gefunden = such_element in daten_set
end_set = time.perf_counter()
zeit_set = end_set - start_set
print(f"Set: {zeit_set:.6f} Sekunden")

# ==============================================================================
