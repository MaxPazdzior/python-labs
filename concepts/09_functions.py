# ==============================================================================

# def hello_world():      # Funktionsdefinition
#     print("Hello World!!")

# def funk_01():
#     a = 5
#     b = 8
#     c = a * b 
#     d = 3 - c
#     print(f"Ergebnis: {d}")

# def quadrat_berechnen(zahl):
#     antwort = zahl * zahl
#     print(f"Antwort: {antwort}")

# def differenz_berechnen(z1, z2):
#     antwort = z1 - z2
#     print(f"Differenz {antwort}")

# def begruessung(name="Gast!"):      # --> Hier geben wir vor, was eingetragen wird, wenn beim Aufruf die Klammer Leer gelassen wird
#     print(f"Hallo, {name}! Schön, dass du da bist.")

# def berechne_brutto(netto_preis):
#     brutto = netto_preis * 1.19
#     return brutto

# def ist_volljaehrig(alter):
#     if alter >= 18:
#         return True
#     else:
#         return False


# Mutability (Veränderbarkeit)
# Mutable: list, dictionary, set
# Immutable: int, float, string, tuple, bool

# def addieren_liste(liste,n):
#     temp = liste.copy()
#     for i in range(len(temp)):
#         temp[i] += n
#     return temp


# Scope (Sichtbarkeitsbereich): local oder global
# ACHTUNG, GEFAHR: Schlechter Programmierstil!

# def funktion_a():
#     y = "Brokkoli"      # --> Das ist local, da es in der Funktion schon definiert wird. Global ist alles außerhalb der Funktion
#     # global x --> Bitte nicht!
#     x = "Tomate"
#     print(y,x)

# ==============================================================================

# Hauptprogramm:

# hello_world()   # Funktionsaufruf

# funk_01()

# quadrat_berechnen(4)        # --> Hier muss jetzt eine Zahl in der Klammer stehen, weil wir oben zahl definiert haben im Programm
# quadrat_berechnen(2)
# for i in range(1,20):
#     quadrat_berechnen(i)        # --> Kann man auch mit SChleifen verbinden

# differenz_berechnen(3,2)

# begruessung("Daniel")

# x = berechne_brutto(20.0)
# print(f"{x:.2f}")

# alter= int(input("Wie alt bist du?"))
# antwort = ist_volljaehrig(alter)
# if antwort:
#     print(f"Du bist aber schon alt... {alter} Jahre alt!")
# else:
#     print("Genieße es noch!")

# meine_zahlen = [5, 2, 9, 1]
# zahlen_neu = addieren_liste(meine_zahlen,2)
# print(f"Neue Liste: {zahlen_neu}")
# print(f"Alte Liste: {meine_zahlen}")

# x = "Kartoffel"     # --> Muss vor dem Aufruf geschrieben werden sonst geht es nicht
# funktion_a()
# print(x)

# ==============================================================================