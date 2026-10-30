# ==============================================================================

import csv

csv_path = "Python/deutschebahn.csv"
trains = []

def analyze_delays(trains):
    delayed_trains = 0
    total_delay = 0
    count_trains = len(trains)

    for train in trains: 
        delay = int(train["VerspätungMin"])      # --> hier wird die info aus dem dict bezogen
        total_delay += delay        # --> Hier werden die Minuten angegeben

        if delay >0:
            delayed_trains += 1

    avg_delay = total_delay / count_trains
    return delayed_trains, avg_delay

try:
    with open(csv_path, mode="r", encoding="UTF-8", newline="") as file:        # --> as file weil wir das mit with öffnen. r also read weil wir nur lesen nichts verändern wollen
        reader = csv.DictReader(file, delimiter=",")       # --> File brauchen wir in der Klammer, weil wir oben das als File deklariert haben
        for row in reader:
            trains.append(row)
except FileNotFoundError:
    print("Datei wurde nicht gefunden.")

if len(trains) >0:
    delayed_trains, avg_delay = analyze_delays(trains)
    print(f"Züge mit Verspätung: {delayed_trains}\nDurchschnittliche Verspätung: {avg_delay:.2f} Minuten")

# ==============================================================================