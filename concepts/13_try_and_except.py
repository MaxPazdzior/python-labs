# ==============================================================================

# Exception Handling = Ausnahmebehandlung
# Kontrolliert reagieren, anstatt unkontrolliert abzustürzen!

# Warum ist Exception Handling wichtig?
#  - Stabilität
#  - Benutzerfreundlichkeit
#  - Wartbarkeit & Debugging

# ==============================================================================

# Fall 1: IndexError

# autos = ["BMW","VW","Audi"]

# try:        # try bedeutet versuche
#     print(autos[3])
# except IndexError:      # scept bedeutet quasi else
#     print("Fehler! Auto existiert nicht!")

# print("Weiter geht es...")

# ==============================================================================

# Fall 2: ValueError

# a = 2 ** 100000     # Das klappt nur das print ist hier das Problem
# try:
#     print(a)
# except ValueError:
#     print("Zahl ist zu groß für den Terminal")

# ==============================================================================

# Fall 3: TypeError

# def add_values (a,b):
#     try:
#         return a + b
#     except TypeError:
#         return "Error: incompatible types!"

# print(add_values(10,"20"))

# ==============================================================================

# Fall 4: KeyError

# capitals = {
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Brazil": "Brasilia"
# }

# country = input("Enter a country name:\n")
# try:
#     capital = capitals[country]
#     print("Gefunden!")
# except KeyError:
#     print("Error")

# ==============================================================================

# Fall 5: ZeroDivisionError

# try:
#     ergebnis = 10 / 0
# except ZeroDivisionError as e:      # Das as e bedeutet, dass in der Konsole dann die Python Fehlermeldung mit ausgegeben wird. --> Fehler! division by zero
#     print(f"Fehler! {e}")
#     print(type(e))

# ==============================================================================

# Fall 6: Generischer Catch-All

# try:
#     # Code Hier
#     import modul_was_nicht_gibt
# except Exception:
#     print("Fehler")

# ==============================================================================

# Fall 7: Fehler ignorieren

# try:
#     import optionales_modul
# except ImportError:
#     pass        # Mit pass wird der Fehler einfach ignoriert

# ==============================================================================

# Fall 8: NameError

# try:
#     print(x)
# except NameError:
#     print("x kenne ich nicht...")

# ==============================================================================

#  ValueError, ZeroDivisionError

# while True:
#     try:
#         zahl1 = float(input("Bitte die erste Zahl eingeben:\n"))
#         zahl2= float(input("Bitte die zweite Zahl eingeben:\n"))
#         ergebnis = zahl1/zahl2
#     except ValueError:      # Hier müssen wir zwei except machen weil zwei Fehler entstehen können
#         print("Bitte nur Zahlen eingeben!!\n")
#     except ZeroDivisionError:       # Hier müssen wir zwei except machen weil zwei Fehler entstehen können
#         print("Bitte keine 0 eingeben!!\n")
#     else:       # Else ist hier das Gegenteil von except
#         print(f"Das ergebnis ist: {ergebnis}")
#         break
#     finally:        # Das hier wird immer ausgegeben
#         print("Das hier kommt immer!!")

# ==============================================================================

# benutzer_daten = {
#     "max_power": {
#     "name": "Max",
#     "kontakt": {"email": "max@email.de", "telefon": "+49123456"}
#     },
#     "anna_123": {
#         "name": "Anna",
#         "kontakt": {"email": "anna@email.de", "telefon": "+49987654"}
#     }
# }

# username = "max_power"
# # username = input()

# try:
#     profil = benutzer_daten[username]
# except KeyError:
#     print(f"Fehler! Das Profil für {username} existiert nicht!")
# else:
#         telefon = profil ["kontakt"]["telefon"]

# ==============================================================================

# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")     # Gibt unsere eigene Fehlermeldung im Terminal aus: Exception: Sorry, no numbers below zero

# def setze_alter(alter):
#     if alter < 0:
#         raise ValueError("Das Alter darf nicht negativ sein!")
#     return alter

# try:
#     setze_alter(-4)
# except ValueError as e:
#     print(f"Eingabefehler: {e}")

# ==============================================================================