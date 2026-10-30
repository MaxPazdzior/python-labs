# ==============================================================================

# datei = open("Python/Abendlied.txt","r",encoding="UTF-8")     # --> Das "r" steht für read. Wir lesen quasi die angegebene Datei. 
# # Das Encoding sorgt dafür, dass es richtig gelesen wird.
# print(datei)
# print(datei.read())     # Hiermit wird es dann im Terminal angezeigt
# print(type(datei.read()))

# datei.seek(0)       # --> Mit Seek wird wieder von neu angefangen. die "0" bedeutet, dass es an der ersten Stelle anfängt
# print(datei.read())     # Beim zweiten mal wird es nichtmehr angezeigt weil es nach einmal ausführen aus dem Cache geleert wird

# datei.seek(0)
# print("\nRead Line:")
# print(datei.readline()[:-1])     # --> Hier wird es pro Zeile gelesen und man kann auch nur eine Zeile ausgeben
# print(datei.readline()[:-1])     # --> "-1" beduetet, dass hier der Zeilenumbruch weg ist. Ansstatt im Terminal mit Enter, steht es wieder normal untereinander
# print(datei.readline()[:-1])

# datei.seek(0)
# print("\nRead Line:")
# print(datei.readline().replace("\n",""))        # --> Ist das gleiche wie darüber mit dem Umbruch
# print(datei.readline().replace("\n",""))
# print(datei.readline().replace("\n",""))

# ==============================================================================

# String strip()
# txt = "...ban.ana.m....."
# print(txt.strip("."))       # --> Strip entfernt das angegebene Zeichen/Buchstaben aus dem vorhandenen Text. Aber nur die ersten und die Letzten
# print(txt.lstrip("."))      # Das l und r stehen für links und rechts
# print(txt.rstrip("."))
# info = "C:/test.pdf"
# print(info.strip("C:/"))

# datei.seek(0)
# for zeile in datei:
#     print(zeile.rstrip())

# ==============================================================================

# datei.seek(0)
# lines = datei.readlines()        # --> Schreibt alles in eine Zeile als Liste
# print(f"\nThe file '{datei.name}' has {len(lines)} lines.")
# print(lines[3].rstrip())

# for i, zeile in enumerate(lines):
#     if i %2 == 0:
#         print(zeile.rstrip())

# datei.close()       # --> Hier wird die Datei wieder geschlossen

# ==============================================================================

# datei = open("Python/Abendlied.txt","w",encoding="UTF-8")
# datei.write("Sabotage")     # --> Löscht den gesammten Text aus der Datei und ersetzt ihn durch das angegebene
# datei.close()

# datei = open("Python/Abendlied.txt","a",encoding="UTF-8")
# datei.write("Sabotage")     # --> Durch das "a" oben fügt man jetzt nur das Wort am Ende hinzu und löscht es nicht mehr
# datei.close()

# ==============================================================================

# datei = open("Python/Abendlied.txt","r",encoding="UTF-8")
# # text = datei.read()         # Ganzer Text
# # line = datei.readline()     # Nur eine Zeile
# lines = datei.readlines()     # Mehrere Zeilen
# # print(lines)
# lines.append("\n\n - Matthias Claudius, 1778")

# datei2 = open("Test.txt","w",encoding="UTF-8")
# datei2.writelines(lines)

# # datei2.seek(0)  
# # print(datei2.readline())    # Das hier geht nicht

# datei.close()
# datei2.close()

# with open("datei.txt","w",encoding="UTF-8") as file:
#     file.write("Hallo Welt!")

# ==============================================================================