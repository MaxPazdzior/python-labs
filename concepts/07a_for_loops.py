# ==============================================================================

# for-Schleife: Zählschleife
# 1) Initialisierung: Zählvariable wird gestartet
# 2) Bedingung
# 3) Schrittweite

# a= "Hallo"

# for i in range(0,5,1):
#     print(a)

# ==============================================================================

# a= "Hallo"

# for i in range(0,5):  # Ist das gleiche wie oben
#     print(a)

# ============================================================================== 

# a = "Hallo"

# for i in range(5):       #Ebenfalls das gleiche wie oben
#     print(a)

# ==============================================================================

# for i in range(1,6):    # Hier wird 1-5 ausgegeben
#     print(i)

# ==============================================================================

# Alle gerade Zahlen von 0 bis 100:

# for i in range (0,101,2):   # Muss bei 101 aufhören da Python immer die 0 mitzählt! 
#     print(i)

# ==============================================================================

# Alle ungerade Zahlen von 1 - 100:

# for i in range(1,101,2):
#     print(i)

# ==============================================================================

# for i in range (5,0,-1):      # Hier wird von 5 - 1 runter gezählt
#     print(i)

# ==============================================================================

# for a in range(1,16):
#     if a % 3== 0:   # Wenn durch 3 Teilbar und gleich 0 dann wird es ausgegeben
#         print(a)

# ==============================================================================

# zaehler = 0
# for a in range(1,16):
#     if a % 3== 0:
#         print(a)
#         zaehler += 1
# print(f"{zaehler}-mal gefunden!")   # Muss genau so eingerückt sein, damit es richtig funktioniert

# ==============================================================================

# for a in range(3,16,3):     # So kann man es auch schreiben wenn man etwas teilen will. Gleiches Ergebnis wie oben
#     print(a)

# ==============================================================================

# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50

# Meine Lösung

# zahl = 0
# for i in range(5,51,5):
#     zahl += 1
#     print(f"{zahl} x 5 = {i}")

# Daniels Lösung

# for i in range(1,11):
#     ergebnis = i * 5
#     print(f"{i} x 5 = {ergebnis}")

# ==============================================================================

# 1 ist ungerade
# 2 ist gerade
# 3 ist ungerade
# 4 ist gerade
# 5 ist ungerade
# 6 ist gerade
# 7 ist ungerade
# 8 ist gerade
# 9 ist ungerade
# 10 ist gerade

# for i in range(1,11):
#     if i % 2 == 0:
#         print(f"{i} ist gerade")
#     else:
#         print(f"{i} ist ungerade")

# ==============================================================================

# °
# °°
# °°°
# °°°°
# °°°°°
# °°°°°°
# °°°°°°°
# °°°°°°°°

# for i in range(1,10):
#     print("°"*i)

# ==============================================================================