# ==============================================================================

# while-Schleife: Kopfgesteuerte Schleife

# zahl = 1
# while zahl <=5:
#     print(zahl)
#     zahl += 1       # Addieren und zuweisen, ist das gleiche wie wenn ich schreiben würde -> zahl = zahl + 1. Deswegen zahl += 1 
#     zahl -= 1       # Nun ist es eine endlose Schleife

# a = 5
# while a != 0:   # != --> Ungleich
#     print(a)
#     a -= 1

# ==============================================================================

# Gib alle gerade Zahlen von 2 bis 8 aus

# n = 2
# while n <= 8:
#     print(n)
#     n += 2

# ==============================================================================

# Starte bei der Zahl 1 und verdopple sie so oft,
# bis sie größer als 20 ist.

# a = 1
# while a <= 32:
#     print(a)
#     a *= 2

# ==============================================================================

# Addiere die Zahlen von 1 bis 6 zusammen und gib das Ergebnis aus

# a = 1
# summe = 0
# while a <= 6:
#     summe += a  # Summe + k --> 1 + 2 + 3 + 4 + 5 + 6
#     a += 1
# print(f"Die Antwort ist: {summe}")

# ==============================================================================

# Multipliziere die Zahl 3 nacheinander mit den Zahlen von 1 bis 5
# Gib die Ergebnisse einzeln aus

# a = 1
# while a <= 5:
#     ergebnis = 3 * a
#     print(f"3 x {a} = {ergebnis}")
#     a +=1

# ==============================================================================

# Lass ein Programm von 5 bis 1 rückwärts zählen
# gib die Zahlen nacheinander aus.
# Am Ende soll das Wort "Start!" ausgegeben werden

# a = 5
# while a >= 1:
#     print(a)
#     a -= 1
# print("Start!")

# ==============================================================================

# while True:
#     antwort = input("Möchten Sie fortfahren? (ja/nein)\n").lower()
#     if antwort == "ja":
#         print("Sehr schön!")
#         break
#     elif antwort =="nein":
#         print("Schade!")
#         break
#     else:
#         print("Ungültig! Bitte ja oder nein eingeben")

# ==============================================================================

# continue:
# - Aktuellen Durchlauf abbrechen! - Nicht die gesammte Schleife wie bei break!!
# - Die Schleife springt zur Bedingung

# zähler = 1
# while zähler < 5:
#     zähler +=1
#     if zähler == 3:
#         continue
#     print(zähler)   # Code nach dem "continue"

# ==============================================================================