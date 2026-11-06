# ============================================================================== 

# Hausaufgabe 01 (random):
# Entwickle ein interaktives Konsolen-Programm in Python, bei dem der Computer eine zufällige Geheimzahl (zwischen 1 und 99) generiert und der Benutzer 
# diese mit logischen Hinweisen ("zu hoch" / "zu niedrig") erraten muss. Am Ende soll die Anzahl der benötigten Versuche ausgegeben werden.


# ============================================================================== 

# Hausaufgabe 02: „Schere, Stein, Papier“ in Python (random):
# Schreiben Sie ein Konsolen-Spiel, bei dem ein Spieler unendlich viele Runden „Schere, Stein, Papier“ gegen den Computer spielen kann, bis er das Spiel bewusst beendet.
 
# - Der Computer wählt in jeder Runde zufällig zwischen „Schere“, „Stein“ oder „Papier“ aus.
# - Der Spieler gibt seine Wahl per Text ein. Die Eingabe muss tolerant gegenüber Groß- und Kleinschreibung sein (z. B. schere wird zu Schere).
# - Ungültige Eingaben werden abgefangen und die Abfrage wiederholt.
# - Das Programm prüft auf Unentschieden, Sieg oder Niederlage gibt das Ergebnis aus.
# - Bei der Eingabe 'Ende' stoppt das Spiel mit einer Abschiedsmeldung.

# ==============================================================================

# Aufgabe 1)

import random

geheimzahl=random.randint(1,99)
versuche = 0

while True:
    user_input=int(input("An welche Zahl denke ich gerade?\n"))
    versuche += 1
    if user_input < geheimzahl:
        print("Zu Niedrig. Versuche es noch einmal!")
    elif user_input > geheimzahl:
        print("Zu hoch. Versuche es noch einmal!")
    elif user_input == geheimzahl:
        print(f"Du hast die richtige Zahl erraten. Es war die {geheimzahl}. Du hast {versuche} Versuche gebraucht.")
        break
    else:
        print("Du hast keine Zahl eingegeben. Versuche es noch einmal.")

# ==============================================================================

# Aufgabe 2)

import random

spiel=["Stein","Schere","Papier"]

while True:
    user_choice=input("Willkommen zu Stein, Schere, Papier.\nGib eins der Wörter ein, wenn du spielen willst. Wenn du beenden willst gib Ende ein.\n").strip().capitalize()

    if user_choice == "Ende":
        print("Danke fürs spielen. Auf wiedersehen!")
        break
    elif (user_choice != "Stein") and (user_choice != "Schere") and (user_choice != "Papier"):
            print("\nDiese Eingabe existiert nicht. Versuche es noch einmal!\n")
            continue


    computer=random.choice(spiel)

    if user_choice == computer:
        print("\nDas war ein unendschieden. Versuch es noch einmal!\n")
    elif (user_choice == "Stein" and computer == "Schere") or (user_choice == "Schere" and computer == "Papier") or (user_choice == "Papier" and computer == "Stein"):
        print(f"\nDu hast gewonnen! {user_choice} schlägt {computer}!\n")
    elif (user_choice == "Stein" and computer == "Papier") or (user_choice == "Schere" and computer == "Stein") or (user_choice == "Papier" and computer == "Schere"):
        print(f"\nDu hast verloren! {user_choice} verliert gegen {computer}\n")

# Erste Lösung
    # if user_choice == "Stein":
    #     if computer == "Stein":
    #         print("Das war ein unendschieden!\n")
    #     elif computer == "Schere":
    #         print("Du hast gewonnen. Stein schlägt die Schere.\n")
    #     elif computer == "Papier":
    #         print("Du hast verloren. Papier schlägt den Stein.\n")
    # elif user_choice == "Schere":
    #     if computer == "Stein":
    #         print("Du hast verloren. Stein schlägt Schere.\n")
    #     elif computer == "Schere":
    #         print("Das war ein unendschieden!\n")
    #     elif computer == "Papier":
    #         print("Du hast gewonnen. Die Schere schlägt das Papier.\n")
    # elif user_choice == "Papier":
    #     if computer == "Stein":
    #         print("Du hast gewonnen. Das Papier schlägt den Stein.\n")
    #     elif computer == "Schere":
    #         print("Du hast verloren. Die Schere schlägt das Papier.\n")
    #     elif computer == "Papier":
    #         print("Das war ein unendschieden!\n")
    # elif user_choice == "Ende":
    #     print("Danke fürs Spielen. Auf wiedersehen!\n")
    #     break
    # else:
    #     print("Dies war keine gültige Eingabe. Versuch es nocheinmal\n")

# ==============================================================================
