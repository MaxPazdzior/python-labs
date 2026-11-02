# ==============================================================================

# Random ist nicht wirklich zufällig!!
# PRNG - Pseudozufallgenerator
# Algorithmus: Mersenne-Twister --> Vorhersehbar!!
# Spieleentwicklung, Simulationen

# ==============================================================================

import random
import secrets      # Strong Pseudo-Random

z1 = random.random()        # --> Float ziwschen 0.0 und < 1.0
print(z1)

# random.seed(20)     # --> Seed wird vergeben. Wenn Menschen den gleichen Seed haben, werden sie die selben Ergebnisse haben obwohl es random ist. 
z2 = random.random()
z3 = random.random()
print(z2,z3)

z4 = random.uniform(2.5,10.5)       # --> Hier wird eine Zufällige Zahl generiert zwischen den beiden in der Klammer
print(z4)

z5 = random.randrange(0,10,2)     # --> Start, Stop und Schrittweite
print(z5)

wuerfel = random.randrange(1,7)     # --> Man muss die 7 angeben, weil er die letzte Zahl nie erreicht.
print(wuerfel)

# ==============================================================================

tiere = ["Hund","Katze","Ameise","Elephant","Bär","Taube"]
print(random.choice(tiere))     # --> Random Wert aus der Liste wird raus geholt
print(random.choices(tiere,k=10))        # --> Choices holt hier mehrere Werte. Hier können aber auch die gleichen mehrfach auftreten
print(random.sample(tiere,k=5))     # --> Das gleiche wie choices, nur dass hier keine doppelten Tiere kommen

tierebacku = tiere.copy()       # --> Macht eine Kopie von der Liste
random.shuffle(tiere)       # "in-place" Operation / Hier wird in der Liste jetzt eine neue Reihenfolge gemacht
print(tiere)

# ==============================================================================

t1 = (1,2,3,4,5,6)
print(random.choice(t1))        # --> Funktioniert wie bei der Liste

# ==============================================================================

s1= "Python"
print(random.choice(s1))        # --> Holt einen Random Buchstabe aus dem String raus und gibt ihn aus

# ==============================================================================

d1 = {"Anna":28, "Paula":32,"Lukas":21}
zufall_schluessel = random.choice(list(d1.keys()))      # --> Ein Dictionarie muss erst in eine Liste umgewandelt werden, damit man choice benutzten kann
print(zufall_schluessel)
print(d1[zufall_schluessel])        # --> Hier wird das Alter der Person ausgegeben

# ==============================================================================

zufallszahl = secrets.randbelow(10)     # --> Hier bekomme ich eine Zufallszahl zwischen 0 und 9
print(zufallszahl)
sicheres_token = secrets.token_hex(16)      # --> Hier wird ein sicherer 16 Stelliger Token generiert
print(sicheres_token)
print(secrets.choice(tiere))        # --> Hier wird ein Random Tier aus der Liste geholt

# ==============================================================================