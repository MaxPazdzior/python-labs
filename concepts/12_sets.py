# ==============================================================================

# Set = Menge
# - Einzigartigkeit. Doppelte Einträge --> automatisch entfernt
# - Ungeordnet!! Keine feste Reihenfolge!! Zugriff über Index nicht möglich.
# - Schnelle Prüfung

# ==============================================================================

# set_01 = {1,2,3}
# dic_01 = {"A":1, "B":2, "C":3}      # --> Das ist der Unterschied von set zu dic

# print(set_01,type(set_01),len(set_01))
# print(dic_01,type(dic_01),len(dic_01))

# ==============================================================================

# set_02 = {[1,2],[4,5],[3,2]}    # Das geht nicht. Lists - Mutable / TypeError: unhashable type: 'list'
# set_02 = {(1,2),(5,2)}      # Das geht, weil es ein Tupel ist
# set_03 = {"A","B","C"}      # Das geht auch
# set_04 = {0,3.14,(2,4)}     # Das geht auch

# print(set_04)

# ==============================================================================

# In Python, bool ist eine Unterklasse von INT!!

# set_05 = {True, False, True, True, False, 5, 3, 2, 1}       # --> Da Einzigartigkeit besteht, wird es nur jeweils einmal ausgegeben. Die 1 wird nicht gespeichert, weil True von Python als 1 gewertet wird
# print(set_05)

# set_05 = {5,6,7,8}
# for x in set_05:
#     print(x)

# print(6 in set_05)      # Gibt True aus, weil die 6 im Set enthalten ist

# if 5 in set_05:
#     print("Gefunden!")

# ==============================================================================

# liste_dop = [1,2,2,5,3,2,1,5,2]
# temp_set = set(liste_dop)       # So kann man eine Liste Filtern und alle doppelten sachen raus nehmen
# print(temp_set)
# liste_einz = list(temp_set)
# print(liste_einz)       # Wandelt das Set wieder in eine Liste um

# ==============================================================================

# dic_leer = {}       # Das ist ein leeres Dictionary
# set_06 = set()      # So erstellt man ein leeres Set, damit sich das nicht mit den Dictionarys unterscheidet
# print(dic_leer,set_06)

# set_06.add(6)       # Anders als mit Listen, wo man .append macht, macht man hier .add
# set_06.add(1)
# set_06.add(7)
# print(set_06)

# # set_06.remove(1)    # So entfernt man etwas aus einem Set. Wenn etwas nicht drin ist aber man will es removen, gibt es ein Fehler
# # print(set_06)

# set_06.discard(3)      # Entfernt den Wert, wenn es ihn gibt. Wenn nicht wird es einfach ignoriert

# if 10 in set_06:
#     set_06.remove(10)
# else:
#     print("10 not found!")

# set_06.clear()      # Cleart das Set
# print(set_06)

# if set_06 == set():     # So kann man prüfen, ob das Set leer ist
#     print("Leer")

# if not set_06:
#     print("Leer")       # So kann man ebenfalls prüfen, ob das Set leer ist

# ==============================================================================

# set_A = {1,2,3,4}
# set_B = {3,4,5,6}
# set_C = {6,7,8,9}

# # Schnittmenge / Intersection
# # Elemente, die in beiden Sets gleichzeitig enthalten sind
# print(set_A.intersection(set_B))        # Hier wird angezeigt welche Elemente die sind, welche in beiden Sets drin vorkommen
# print(set_A & set_B)        # Das ist das gleiche nur kürzer

# # Vereinigungsmenge / Union
# # Alle Elemente aus beiden Sets
# print(set_A.union(set_B))       # Hier wird angezeigt was alles in den Sets drin ist. Doppelte werden raus genommen
# print(set_A | set_B)        # Ist beides das gleiche

# # Differenz:
# # Zieht alle Elemente von set_B aus set_a ab.
# print(set_A.difference(set_B))      # Hier wird die Differenz gemacht zwischen den Sets
# print(set_A - set_B)

# # Symetrische Differenz:
# # Elemente, die ENTWEDER NUR in A oder B sind
# print(set_A.symmetric_difference(set_B))
# print(set_A ^ set_B ^ set_C)

# ==============================================================================

# tag_1 = ["Anna", "Ben", "Charlie", "Anna", "Diana", "Ben"]
# tag_2 = ["Charlie", "Erik", "Flora", "Diana", "Diana", "Gabriel"]
 
# 1) Bereinigung: Entferne alle Duplikate aus den einzelnen Tageslisten mithilfe von Sets
# 2) Gesamte Besucher: Erstelle eine Liste aller einzigartigen Personen, die das Festival überhaupt besucht haben.
# 3) Nur Tag 1: Finde die Personen heraus, die nur am ersten Tag da waren und den zweiten Tag verpasst haben.
# 4) Stammgäste: Finde heraus, welche Personen an beiden Tagen da waren.
# 5) Finde alle Personen, die nur an einem Tag da waren (1. oder 2.)

# Lösung

# # Aufgabe 1)
# tag1 = set(tag_1)
# tag2 = set(tag_2)

# print(f"Besucher Tag 1: {tag1}\nBesucher Tag 2: {tag2}")

# # Aufgabe 2)
# einzigartig = list(tag1 | tag2)
# print(f"Die einzigartigen Besucher sind: {einzigartig}")

# # Aufgabe 3)
# differenz = list(tag1 - tag2)
# print(f"Den zweiten Tag haben folgende Personen verpasst: {differenz}")

# # Aufgabe 4)
# schnittmenge = list(tag1 & tag2)
# print(f"Die Stammgäste beider Tage waren: {schnittmenge}")

# # Aufgabe 5)
# symetrischedifferenz = tag1 ^ tag2
# print(f"An nur einem Tag da waren folgende Personen: {symetrischedifferenz}")

# ==============================================================================

# 1. Das „Oder“-Zeichen: | (Pipe)
#  • Name: Vereinigung (Union)
#  • Bedeutung: Gibt alle Personen zurück, die an Tag 1 oder an Tag 2 (oder an beiden Tagen) da waren. Es wirft automatisch alle doppelten Namen raus.
#  • Merkhilfe: Das Zeichen steht für „Alles in einen Topf“.
#  • Code: tag1 | tag2

# 2. Das „Und“-Zeichen: & (Kaufmännisches Und / Ampersand)
#  • Name: Schnittmenge (Intersection)
#  • Bedeutung: Gibt nur die Personen zurück, die an Tag 1 und an Tag 2 da waren (die Stammgäste).
#  • Merkhilfe: Das & verbindet beide Tage – wer war an beiden da?
#  • Code: tag1 & tag2

# 3. Das Minus-Zeichen: -
#  • Name: Differenz (Difference)
#  • Bedeutung: Zieht alle Personen von Tag 2 von Tag 1 ab. Übrig bleiben die Personen, die nur an Tag 1 da waren und Tag 2 verpasst haben.
#  • Wichtig: Die Reihenfolge zählt! tag2 - tag1 würde die Personen zeigen, die nur an Tag 2 da waren.
#  • Merkhilfe: Ganz normales Abziehen wie beim Rechnen.
#  • Code: tag1 - tag2

# 4. Das „Entweder-Oder“-Zeichen: ^ (Caret / Dach-Zeichen)
#  • Name: Symmetrische Differenz (Symmetric Difference)
#  • Bedeutung: Gibt alle Personen zurück, die nur an einem einzigen Tag da waren. Die Stammgäste (die an beiden Tagen da waren) fliegen komplett raus.
#  • Merkhilfe: Das Zeichen sieht aus wie ein Pfeil nach oben, der die Schnittmenge „aushebelt“ (wegschmeißt).
#  • Code: tag1 ^ tag2

# ==============================================================================

# benoetigte_skills = {"python", "git"}
# bewerber_skills = {"python", "git", "docker", "linux"}

# # Hat der Bewerber alle benötigten Skills?
# ist_qualifiziet = benoetigte_skills.issubset(bewerber_skills)       # Hier wird nachgeschaut, ob das eine Set im anderen erhalten ist. Gibt True oder False aus
# if ist_qualifiziet:
#     print("Ist qualifiziert")
# else:
#     print("Leider nicht qualifiziert")


# # Mengen besitzen keine gemeinsame Elemente:
# warenkorb = {"Ladekabel", "Handyhülle", "Powerbank"}
# gefahrgut_liste=["Sprühdose", "Powerbank", "Feuerwerk"]
# print(warenkorb.isdisjoint(gefahrgut_liste))        # Überprüft ob die Listen unterschiedlich sind. Gibt True oder False aus


# set_A = {4,76,7,3,21,-6}
# print(max(set_A))
# print(min(set_A))
# print(sum(set_A))


# fruits = {"apple", "banana"}
# new_fruits = ["cherry", "mango", "apple"]
# fruits.update(new_fruits)       # Fügt die Sachen welche noch nicht im Set drin sind hinzu
# print(fruits)

# a = {1,2,3}
# a |= {4,5}      # Das ist auch ein Update 
# print(a)


# # Pop
# s = {100,200,300,400}
# popped =s.pop()     # Hier wird ein Element entfernt
# print(f"Popped: {popped}, Set: {s}")

# verbindungen_set = {"Verbindung_A","Verbindung_B","Verbindung_C"}
# verbindungen_list = ["Verbindung_A","Verbindung_B","Verbindung_C"]

# while verbindungen_set:
#     conn = verbindungen_set.pop()
#     print(f"Schließe und trenne {conn}...(SET)")    # Bei Set wird die Ausgabe Random generiert

# while verbindungen_list:
#     conn = verbindungen_list.pop()      # Bei Listen wird es bei der Ausgabe vom letzten zum ersten gemacht. Macht man eine 0 in die Klammer geht es von A-C 
#     print(f"Schließe und trenne {conn}... (LIST)")


# # Frozensets
# fs = frozenset({3,2,6,4})

# routen = {
#     frozenset({"Berlin", "München"}):500,
#     frozenset({"Paris","Berlin"}):1050
# }

# print(routen[frozenset({"Berlin","Paris"})])

# ==============================================================================