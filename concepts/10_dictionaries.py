# ==============================================================================

# Datentyp: Dictionary
# Struktur --> "Schlüssel: Wort"  (Key: Value)

# auto_dict = {       # Kann man mit mehr Aufwand auch mit Listen machen. Siehe darunter
#     "Marke": "Ford", 
#     "Modell": "Mustang", 
#     "Bahjahr": 1964,
#     "Kaufjahr": 1964 
# #    "Baujahr": 1970     # Es darf keinen doppelten Wert geben, weil es immer nur ein Primary key geben darf           
# }

# # auto_list = ["Fort","Mustang", 1964]

# # auto_info = ["Marke","Modell","Baujahr"]

# # print(auto_dict)
# # print(type(auto_dict))
# print(auto_dict["Marke"])
# # print(auto_dict["Mark"])  # Das ist ein Key-Error

# if "Marke" in auto_dict:
#     print(f"Die Marke ist {auto_dict["Marke"]}")
# else:
#     print("Schlüssel nicht gefunden")

# if "Mustang" in auto_dict.values():     # Holt die Schlüssel aus dem Dict.
#     print("I have a Mustang")
# else:
#     print("I have a Camaro")

# print(len(auto_dict))

# print(auto_dict)
# auto_dict["Farbe"] = "Rot"      # Hinzufügen
# print(auto_dict)
# auto_dict["Farbe"] = "Blau"     # Würde Farbe Rot überschreiben weil es nur ein Primary Key gibt
# print(auto_dict)
# print(auto_dict.pop("Farbe"))       # Pop löscht den Key aus dem Dict
# print(auto_dict)
# auto_dict.clear()       # Mit clear leerst du das komplette Dict
# print(auto_dict)

# dict_01 = {}    # Das ist ein leeres Dict

# ==============================================================================

# einkaufsliste = {
#     "Milch": 1.19,
#     "Vollkornbrot": 2.45,
#     "Bio-Eier": 3.99,
#     "Äpfel (1kg)": 2.95
# }

# for produkt,preis in einkaufsliste.items():
#     if "bio" in produkt.lower():        # .lower damit alles in klein convertiert wird und hier suchen wir dann nach dem kleinen bio
#         continue
#     else:
#         preis += preis*0.2      # Hier bekommen Alle sachen außer die Bio sachen 20% auf den Preis dazu 
#         einkaufsliste[produkt] = preis      # Hier müssen wir den Preis nochmal speichern, damit die Änderung auch übernommen wird

# print("--- Einkaufsliste ---")
# for produkt,preis in einkaufsliste.items():     # Elementschleife und Dict's
#     print(f"- {produkt:15} € {preis:.2f}")          # :15 für 15 Abstände im Print damit es besser aussieht

# ==============================================================================

# ergebnis_olympiade ={
#     "Bronze": 3,
#     "Silber": 1
# }

# ergebnis_olympiade["Bronze"] +=1    # Rechnet den Bronze zähler eins weiter hoch
# ergebnis_olympiade["Gold"] =1       # Fügt Gold ins Dict hinzu

# if "Gold" in ergebnis_olympiade:
#     print("Super!!")
# else:
#     print("Noch kein Gold, aber kommt bestimmt noch!")

# if ergebnis_olympiade["Bronze"] >3:
#     print("Sehr gut, mehr als 3x Bronze!")
# else:
#     print("Noch nicht")

# ==============================================================================

# String Split

# txt = "I am very happy."
# x = txt.split()     # Trennt in der Ausgabe alle Wörter aus dem Text, wo ein Lerrzeichen ist in eine Liste. Ausgabe: ['I', 'am', 'very', 'happy.']
# print(x)
# txt2 = "Frankfurt#Las Vegas#Rio de Janeiro#Fukushima"
# print(txt2.split("#"))      # Jetzt wird nichtmehr das Leerzeichen getrennt, sondern alles was neben einem "#" steht
# txt3 = "Hello, my name is Peter, I am 26 years old."
# print(txt3.split(", "))

# ==============================================================================

# text = "apfel banane apfel orange apfel mango banane"
# ergebnis = {}

# for wort in text.split():
#     if wort not in ergebnis:
#         ergebnis[wort] = 1
#     else:
#         ergebnis[wort] +=1

# print(ergebnis)

# ==============================================================================

# klassenbuch = {
#     "Anna": [1.3, 2.0, 1.7],
#     "Ben": [4.5, 3.7, 4.0],
#     "Chris": [5.0, 4.3, 5.3],
#     "Diana": [2.3, 3.0, 2.7]
# }

# # print(klassenbuch["Anna"][1])

# alle_durchschnitte = []

# for name, noten in klassenbuch.items():
#     schnitt = sum(noten) / len(noten)
#     alle_durchschnitte.append(schnitt)
#     print(f"{name:6}: Durchschnitt: {schnitt:3.2f}")

# klassenschnitt = sum(alle_durchschnitte) / len(alle_durchschnitte)
# print(f"Gesamtdurchschnitt der Klasse: {klassenschnitt:.2f}")

# ==============================================================================

# staedte = ["Berlin", "Paris", "London"]
# einwohner = [3.7, 2.1, 8.9]

# staedte_dict = dict(zip(staedte,einwohner))
# print(staedte_dict)

# ==============================================================================

# hotel_zimmer = {
#     "101": {"typ": "Einzelzimmer", "preis": 75, "status": "belegt"},
#     "102": {"typ": "Doppelzimmer", "preis": 120, "status": "frei"},
#     "201": {"typ": "Suite", "preis": 250, "status": "belegt"},
#     "202": {"typ": "Doppelzimmer", "preis": 120, "status": "frei"}
# }

# print(hotel_zimmer["101"])

# ==============================================================================