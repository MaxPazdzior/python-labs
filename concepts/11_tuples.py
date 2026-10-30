# ==============================================================================

# Deutsch: Tupel
# Englisch Tuple (Tuples)

# Ein Tuple ist eine geordnete Reihenfolge von Elementen --> (1,2,3) != (3,2,1)
# Wiederholungen sind erlaubt --> (1,1,1)

# ==============================================================================

# tupel_01 = (1,2,3)
# print(tupel_01)
# tupel_02 = 1,2,3
# print(tupel_02)

# zahl_01 = 2.4   # --> Float wegen "."
# zahl_02 = 2,4   # --> Tuple wegen ","
# print(type(zahl_01))    # --> <class 'float'>
# print(type(zahl_02))    # --> <class 'tuple'>

# zahl_03 = (5)   # --> <class 'int'>
# print(type(zahl_03))

# ==============================================================================

# Sonderfälle

# tupel_03 = ()   # --> Tupel mit "0" Elementen
# print(tupel_03)     # --> Ausgabe: ()
# print(type(tupel_03))   # --> <class 'tuple'>

# tupel_04 = (1,)     # --> Kein int mehr wegen "," nun ist es ein Ein-Element-Tupel --> Singleton
# print(tupel_04)     # --> (1,)
# print(type(tupel_04))   # --> <class 'tuple'>

# ==============================================================================

# Unterschied zwischen Tupel und Listen

# tupel_05 = (1,2,3,4,5,6,7,8,9)
# liste_05 = [1,2,3,4,5,6,7,8,9]

# print(tupel_05[1],liste_05[1])      # Ausgabe bleibt hier die gleiche und ruft man auch gleich ab
# print(len(tupel_05),len(liste_05))      # Ebenfalls gleiche Ausgabe

# liste_05[1] += 1    # Das geht weil es eine Liste ist --> Mutable!
# print(liste_05)
# # tupel_05[1] += 1    # Das geht nicht --> TypeError: 'tuple' object does not support item assignment --> Immutable!!
# # print(tupel_05)

# liste_temp = list(tupel_05)     # Hier machen wir unseren Tupel zu einer Liste, damit wir sie bearbeiten können
# for i in range(len(liste_temp)):
#     liste_temp[i] += 1
# tupel_06 = tuple(liste_temp)    # Hier wird es wieder zu einem Tupel konvertiert
# print(tupel_06)

# ==============================================================================

# Mutable: Listen, Dictionaries(Außer die Schlüssel), Sets
# Immutable: Tupel, Int, Float, Strings, Boolean

# a = 1
# b = 2
# c = a + b
# a = a + 1   # Hier wird das erste a von oben gelöscht und durch dieses hier ersetzt

# ==============================================================================

# points = [(8,6),(1,0),(2,3),(1,1),(5,7)]    # Tupel in einer Liste speichern geht --> Man kann sie aber nicht verändern
# print(points[1][0])     # Tupel 1 Position 0
# # points[1][0] = 2    # Das geht nicht!! --> TypeError: 'tuple' object does not support item assignment
# points[1] = (2,0)   # Das geht
# print(points)

# ==============================================================================

# Sollte man nicht machen:

# tupel_crazy = (1, "Text", [1,2,3])      # Nicht machen!! --> Konflikt entsteht weil nun die Liste in einem Tupel ist!

# ==============================================================================

# Unpacking (Entpacken von Tupeln)

# point = (3,4,5)
# x,y,z = point   # Unpacking
# print(x)

# def get_user_profile():
#     return "Anna", 28, "Berlin"     # Das wird ein Tupel, weil wir Kommas benutzt haben

# name, alter, stadt = get_user_profile()      # Unpacking
# print(name)

# a = 5
# b = 10

# # a = b   # Die beiden würden nicht gehen
# # b = a

# a,b = b,a

# ==============================================================================

# Extended Unpacking --> Sternchen-Operator "*"

# daten = ("2026", "13:30", 22.5, 33.5, 11.1) # --> Die ersten beiden sind nur als String, weil Daniel zeigen wollte, dass es geht
# jahr, uhrzeit, *messungen = daten
# print(uhrzeit)
# print(messungen)

# ==============================================================================

# Schleifen/IF mit "in"

# points = [(8,6),(1,0),(2,3),(1,1),(5,7)]

# for x,y in points:
#     print(f"x={x}, y={y}")

# ampel = ["Rot", "Gelb", "Grün"]
# for index, farbe in enumerate(ampel):
#     print(f"Stufe {index}: {farbe}")

# for mein_tupel in enumerate(ampel):
#     print(mein_tupel)

# ==============================================================================

# RGB-Farbe
# Farbe_Revolution = (255,0,0)    # Älterer Weg
# Farbe_02 = "#05F80D"        # Neuer Moderner Weg
# Server_config = ("127.0.0.1", 8080)

# ==============================================================================

# schueler = ["Alex", "Ben", "Clara", "Daniela"]
# noten = [2,4,1,3]

# schueler_noten = list(zip(schueler,noten))
# print(schueler_noten)

# ==============================================================================

# Tupel als Schlüssel in einem Dict

# Beispiel 01: Tupel als Koordinaten-Schlüssel

# landkarte = {
#     (0,0): "Startpunkt",
#     (1,5): "Schatzkiste",
#     (3,-2): "Falle",
#     (10,10): "Ein alter Turm"
# }

# print("--- Willkommen auf der digitalen Landkarte ---")

# eingabe_x = int(input("Gib die X-Koordinate ein:\n"))
# eingabe_y = int(input("Gib die Y-Koordinate ein:\n"))

# gesuchte_koordinate = (eingabe_x, eingabe_y)

# ort = landkarte.get(gesuchte_koordinate, "Nichts als Sand")

# print(f"\nDu schaust auf Koordinate {gesuchte_koordinate} nach...")
# print(f"Ergebnis: {ort}")

# ==============================================================================

# Beispiele: Leeres Tupel

# 1. Als Standardargument in Funktionen

# def process_data(users=()):
#     for user in users:
#         print(f"Verarbeite: {user}")

# process_data()

# ==============================================================================

# Rückgabewert

# def get_coordinates(city_name):
#     database = {
#         "Blumenau": (36.5,21.6),
#         "Altenfels": (12.6,51.9)
#     }
#     if city_name not in database:
#         return ()
#     else:
#         return database[city_name]

# print(get_coordinates("Blumsenau"))

# ==============================================================================

# 3. Als Schlüssel in einem Dict

# navigation = {
#     (): "Startseite",
#     ("settings",): "Einstellungen",
#     ("settings","profile"): "Profil bearbeiten",
#     ("settings", "passwort"): "Passwort ändern"
# }

# print(navigation[()])
# print(navigation[("settings",)])
# print(navigation[("settings","profile")])
# print(navigation[("settings", "passwort")])

# ==============================================================================