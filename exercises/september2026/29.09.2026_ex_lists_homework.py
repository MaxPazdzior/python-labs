# ==============================================================================

# Aufgabe 01: Ein Delfin-Forschungsprojekt

# Ein Forschungsteam hat die Schwimmgeschwindigkeiten eines Delfins bei verschiedenen Sprints in Kilometern pro Stunde (km/h) gemessen.

# Nutze diese Startliste:
# geschwindigkeiten = [32.5, 41.2, 28.0, 35.8, 43.5, 39.1]

# Deine Aufgabe ist es, die Messungen zu protokollieren. Das Team hat zwei Vorgaben:

# 1. Der Meilenstein: Jede 3. gültige Messung (also Forschungs-ID 3, 6, 9...) ist ein besonderer "Messpunkt-Meilenstein", bei dem die Forscher die Daten intensiver prüfen. 
# Das soll im Code markiert werden.

# 2. Der Rekord: Wenn ein Delfin schneller als 40 km/h schwimmt, gilt das als "Sprint-Rekord".
 
# So soll das Ergebnis in der Konsole aussehen:
 
 
# --- MESSPROTOKOLL GESCHWINDIGKEIT ---
# Forschungs-ID 1: 32.5 km/h -> (Normales Tempo)
# Forschungs-ID 2: 41.2 km/h -> (Sprint-Rekord!)
# Forschungs-ID 3: 28.0 km/h -> (Normales Tempo) [MEILENSTEIN]
# Forschungs-ID 4: 35.8 km/h -> (Normales Tempo)
# Forschungs-ID 5: 43.5 km/h -> (Sprint-Rekord!)
# Forschungs-ID 6: 39.1 km/h -> (Normales Tempo) [MEILENSTEIN]

# Lösung

geschwindigkeiten = [32.5, 41.2, 28.0, 35.8, 43.5, 39.1]
print("\n--- MESSPROTOKOLL GESCHWINDIGKEIT ---")

for index, geschwindigkeit in enumerate(geschwindigkeiten, start =1):

    if geschwindigkeit > 40:
        tempo_text = "(Sprint-Rekord!)"
    elif geschwindigkeit < 40:
        tempo_text = "(Normales Tempo)"

    if index % 3 == 0:
        meilenstein_text = "[Meilenstein]"
    else:
        meilenstein_text = ""

    print(f"Forschungs-ID {index}: {geschwindigkeit} km/h -> {tempo_text} {meilenstein_text}")
    
# ==============================================================================

# Aufgabe 02: To-Do-Listen
# Stell dir vor, du hast eine vorgegebene To-Do-Liste.
# Dein Programm soll den Nutzer in einer while-Schleife nacheinander fragen, ob er die jeweilige Aufgabe bereits erledigt hat.
# Am Ende (oder beim Abbrechen) wird ein Statusbericht ausgegeben.
 
# Die Vorgaben für deinen Code:
# 1. Nutze diese Startliste: todos = ["Einkaufen gehen", "Code schreiben", "Sport machen", "Wäsche waschen"]
# 2. Schleife: Das Programm läuft, solange noch Aufgaben in der Liste offen sind oder bis der Nutzer exit eintippt.
# 3. Nummerierung (enumerate): Nutze enumerate(), um dem Nutzer die aktuelle Aufgabe mit ihrer Nummer (startend bei 1) anzuzeigen.
# 4. Entscheidung (if-else):
# 	• Tippt der Nutzer ja, wird die Aufgabe als erledigt markiert (z. B. durch ein [X] vor dem Namen).
# 	• Tippt der Nutzer nein, bleibt sie offen.
# 	• Tippt der Nutzer exit, bricht die Schleife sofort ab.
# 5. Ausgabe (f-strings): Jede Frage an den Nutzer und die finale Zusammenfassung müssen per f-string formatiert sein.

# Ein möglicher Ablauf in der Konsole:
 
# Aktuelle Aufgabe 1: Einkaufen gehen
# Hast du das erledigt? (ja/nein/exit): ja
# Aktuelle Aufgabe 2: Code schreiben
# Hast du das erledigt? (ja/nein/exit): nein
# Aktuelle Aufgabe 3: Sport machen
# Hast du das erledigt? (ja/nein/exit): exit
# --- DEIN STATUS ---
# [X] 1. Einkaufen gehen
# [ ] 2. Code schreiben
# [ ] 3. Sport machen
# [ ] 4. Wäsche waschen

# Lösung

todos = ["Einkaufen gehen", "Code schreiben", "Sport machen", "Wäsche waschen"]
erledigt = []
programm = True

while programm == True:
    for i, todo in enumerate(todos, start=1):
        if todo in erledigt:
            continue

        eingabe = input(f"Aktuelle Aufgabe {i}: {todo}\nHast du das erledigt? (ja/nein/exit)\n")

        
        if eingabe == "exit":
            programm = False
            break
        elif eingabe == "ja":
            erledigt.append(todo)
        elif eingabe == "nein":
            continue
        else:
            print("Diese Eingabe gibt es nicht!")
            programm = False
            break

    if len(erledigt) == len(todos):
        programm = False

print("--- DEIN STATUS ---")

for i, todo in enumerate(todos, start=1):
    if todo in erledigt:
        haken = "[X]"
    else:
        haken = "[]"

    print(f"{haken} {i} {todo}")

# ==============================================================================
