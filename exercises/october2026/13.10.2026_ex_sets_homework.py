# ==============================================================================

# projekt_web = ["JavaScript", "Python", "TypeScript", "JavaScript", "HTML", "Python"]
# projekt_app = ["Kotlin", "Swift", "TypeScript", "Kotlin", "Java", "Swift"]
# projekt_data = ["Python", "R", "SQL", "Python", "Java", "SQL"]
 
# # 1. Entferne alle Duplikate aus den drei einzelnen Projekt-Listen mithilfe von Sets.
# # 2. Erstelle eine Übersicht (Set oder Liste) aller einzigartigen Programmiersprachen, 
# #    die im gesamten Unternehmen (über alle 3 Projekte hinweg) eingesetzt werden.
# # 3. Finde die Sprachen heraus, die nur im Web-Projekt genutzt werden und in keinem der anderen beiden Projekte vorkommen.
# # 4. Finde heraus, welche Programmiersprachen in allen drei Projekten gleichzeitig eingesetzt werden (falls es welche gibt).

# Lösung 
# Aufgabe 1)
projektw = set(projekt_web)
projekta = set(projekt_app)
projektd = set(projekt_data)

print(projektw,projekta,projektd)

# Aufgabe 2)
einzigartig = list(projektw | projekta | projektd)
print(f"Die einzigartigen Programmiersprachen, welche man braucht sind: {einzigartig}")

# Aufgabe 3)
web = list(projektw - projekta - projektd)
print(f"Die Sprachen, welche nur im Web Projekt benutzt werden sind: {web}")

# Aufgabe 4)
gleichzeitig = list(projektw & projekta & projektd)
print(f"Die Programmiersprache, welche in allen Projekten vorkommt ist: {gleichzeitig}")


# ==============================================================================

# Hausaufgabe 01: Allergie-Checker
 
# Du programmierst einen intelligenten Küchen-Assistenten. Für ein neues Rezept hast du zwei Zutatenlisten als Sets definiert: 
# Die Basis-Zutaten für den Teig und die Zutaten für das Topping. Ein Gast hat eine Allergie und möchte vor dem Essen wissen, 
# ob eine bestimmte Zutat im Gericht enthalten ist und wenn ja, an welcher Stelle.
 
# Gegebene Daten:
# teig_zutaten = {"Mehl", "Milch", "Ei", "Zucker", "Butter"}
# topping_zutaten = {"Erdbeeren", "Schokolade", "Sahne", "Zucker", "Nüsse"}
 
# Schreibe ein Programm, das eine Zutat über input() abfragt. Nutze anschließend if/elif/else-Bedingungen und Set-Operationen, um herauszufinden, wo die Zutat vorkommt.
# Das Programm soll eine der folgenden vier Antworten ausgeben:

# 1. "Warnung: Diese Zutat steckt sowohl im Teig als auch im Topping!": Wenn die Zutat in beiden Sets existiert.
# 2. "Achtung: Diese Zutat ist im Teig enthalten.": Wenn die Zutat nur im Teig vorkommt.
# 3. "Achtung: Diese Zutat ist im Topping enthalten.": Wenn die Zutat nur im Topping vorkommt.
# 4. "Entwarnung: Diese Zutat ist nicht im Rezept enthalten.": Wenn die Zutat in keinem der beiden Sets existiert.

# Lösung
teig_zutaten = {"Mehl", "Milch", "Ei", "Zucker", "Butter"}
topping_zutaten = {"Erdbeeren", "Schokolade", "Sahne", "Zucker", "Nüsse"}

beide = teig_zutaten & topping_zutaten

while True:
    eingabe = input("Gib eine Zutat ein, welche du suchen möchtest:\n").capitalize()

    if eingabe in beide:
        print("Warnung: Diese Zutat steckt sowohl im Teig, als auch im Topping")
    elif eingabe in teig_zutaten:
        print("Achtung: Diese Zutat ist im Teig enthalten")
    elif eingabe in topping_zutaten:
        print("Achtung: Diese Zutat ist im Topping enthalten")
    else:
        print("Entwarnung: Diese Zutat ist nicht im Rezept enthalten.")

# ==============================================================================

# Hausaufgabe 2: Social-Media-Analysator
 
# Du arbeitest für eine Social-Media-Plattform und sollst eine Funktion schreiben, die das Nutzerverhalten analysiert. 
# Dir liegen die User-IDs von drei verschiedenen Aktivitätsgruppen als Listen vor:
# 1. posted_today: Nutzer, die heute etwas gepostet haben.
# 2. liked_today: Nutzer, die heute einen Beitrag geliked haben.
# 3. churned_users: Nutzer, die ihr Konto gelöscht haben.
 
# Deine Aufgabe:

# Schreibe eine Funktion analyse_users(posted_today, liked_today, churned_users), die ein Dictionary mit genau drei Paaren zurückgibt:
# • "super_active": Ein Set mit User-IDs, die heute sowohl gepostet als auch geliked haben (und nicht gelöscht sind).
# • "silent_readers": Ein Set mit User-IDs, die heute nur geliked, aber nicht gepostet haben (und nicht gelöscht sind).
# • "cleanup_needed": Ein Set mit User-IDs, die in den heutigen Aktivitäten (posted_today oder liked_today) auftauchen, 
# obwohl sie eigentlich als gelöscht (churned_users) markiert sind.
 
# # --- Beispieldaten ---
# posted = [101, 102, 105, 101]  # 101 ist doppelt
# liked = [102, 103, 105, 106]
# churned = [105, 107]
 
# Ergebnis: {'super_active': {102}, 'silent_readers': {106, 103}, 'cleanup_needed': {105}}

# Lösung

def analyse_users(posted_today, liked_today, churned_users):
    super_active = (set(posted_today) & set(liked_today)) - set(churned_users)
    silent_readers = (set(liked_today) - set(posted_today)) - set(churned_users) 
    cleanup_needed = (set(posted_today) | set(liked_today)) & set(churned_users)
    return {"super_active":super_active,
            "silent_readers":silent_readers,
            "cleanup_needed":cleanup_needed}

posted = [101, 102, 105, 101]
liked = [102, 103, 105, 106]
churned = [105, 107]
analyse_users(posted, liked, churned)
ergebnis = analyse_users(posted, liked, churned)
print(f"{ergebnis}")

# ==============================================================================

# Aufgabe 03: Ein Rezept-Analysetool (mit FROZENSETS)
 
# Schreibe eine Python-Funktion namens finde_rezepte(verfuegbare_zutaten, rezept_datenbank), die folgendes leistet:
# 1. Die rezept_datenbank ist ein Dictionary. Die Schlüssel sind frozenset-Objekte, die eine Gruppe von Zutaten repräsentieren. 
# Die Werte sind die Namen der Rezepte (Strings).
# 2. Der Parameter verfuegbare_zutaten ist eine normale Liste oder ein Set von Zutaten, die der Nutzer im Kühlschrank hat.
# 3. Die Funktion soll alle Rezepte aus der Datenbank finden, die der Nutzer mit seinen vorhandenen Zutaten kochen kann. 
# Ein Rezept ist kochbar, wenn alle für das Rezept benötigten Zutaten in den verfuegbaren_zutaten enthalten sind.
# 4. Die Funktion soll eine Liste aller passenden Rezeptnamen zurückgeben. Wenn kein Rezept passt, wird eine leere Liste zurückgegeben.
 
# # Vorgegebener Code-Rahmen:

def finde_rezepte(verfuegbare_zutaten, rezept_datenbank):
    kochbuch = rezept_datenbank
    zutatenliste = set(verfuegbare_zutaten)
    rezeptliste = []
    for zutaten, rezeptname in kochbuch.items():
        if zutaten.issubset(zutatenliste):
            rezeptliste.append(rezeptname)
            continue
    return rezeptliste



# # --- TESTDATEN ---

 # Die Rezept-Datenbank nutzt frozensets als Schlüssel
kochbuch = {
    frozenset(["Nudeln", "Tomaten", "Knoblauch"]): "Spaghetti Pomodoro",
    frozenset(["Ei", "Speck", "Nudeln", "Käse"]): "Spaghetti Carbonara",
    frozenset(["Tomaten", "Mozzarella", "Basilikum"]): "Tomate-Mozzarella-Salat",
    frozenset(["Milch", "Mehl", "Ei"]): "Pfannkuchen",
}

# Testlauf 1: Der Nutzer hat Zutaten für Salat und Spaghetti Pomodoro
mein_kuehlschrank_1 = ["Tomaten", "Knoblauch", "Nudeln", "Mozzarella", "Basilikum", "Zucker"]
print(finde_rezepte(mein_kuehlschrank_1, kochbuch))
# Erwartete Ausgabe: ['Spaghetti Pomodoro', 'Tomate-Mozzarella-Salat'] (Reihenfolge egal)

# Testlauf 2: Der Nutzer hat nicht genug Zutaten für Carbonara
mein_kuehlschrank_2 = ["Ei", "Nudeln", "Käse"]
print(finde_rezepte(mein_kuehlschrank_2, kochbuch))
# Erwartete Ausgabe: []

# ==============================================================================
