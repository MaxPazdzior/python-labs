# ==============================================================================

# my_list = [1,5,3,7,6]
# print(my_list)      # --> Gibt aus, was in der Liste steht
# print(type(my_list))    # --> Zeigt den type 
# print(my_list[1])   # --> Gibt die Zahl aus (hier 5 weil es bei 0 anfängt)
# print(my_list[-1])  # --> Gibt die letzte Zahl aus weil er nun rückwärts zählt

# print(len(my_list))     # --> len = lenght = gibt die Länge an wie viel in der Liste drin ist
# # print (my_list[5])    --> Index Error!!
# print(type(my_list[1]))     # --> Gibt an welcher type sich an Position 1 der Liste befindet

# my_list_2 = [1.5,1.4,1.2]       # --> Float Liste
# my_list_3 = ["BMW", "Audi", "Porsche"]      # --> String Liste
# my_list_4 = ["Deutschland",1,3.14,False]    # --> Gemischte Liste

# print(my_list[1:3])     # --> Hier werden die Elemente 1-2 angezeigt. 3 Nicht!!
# print(my_list[:4])      # --> Lässt man die erste Zahl weg, fängt er Automatisch bei 0 an
# print(my_list[3:])      # --> Hier startet er bei der Zahl vorne und geht bis zum Ende

# my_list_3.append("Mercedes")        # --> append fügt etwas ans Ende der Tablle ein
# print(my_list_3)
# my_list_3.remove("BMW")     # --> remove entfernt etwas aus der Liste
# print(my_list_3)
# print (my_list_3.pop())     # --> Entfernt immer das letzt Element
# print(my_list_3)

# for z in my_list:       # --> Zeigt alles was in der Liste steht | --> Elementschleife
#     print(z)

# for i in range(len(my_list)):       # --> Zählschleife  | Zählt wie viel in der Liste drin ist
#     print(i)

# matrix_a = [[1,2,3],[4,5,6]]

# preise = [2.50,1.20,5.00,3.00,0.80]

# print(sum(preise))      # --> sum gibt die Summe der Liste aus

# teuerste_preis = max(preise)    # --> Gibt den Wert der Liste an der am Höhsten ist
# billigster_preis = min(preise)  # --> Gibt den Wert der Liste an der am niedrigsten ist

# print(f"Der teuerste Artikel kostet: {teuerste_preis}")

# preise.sort()   # --> Sortiert die Liste von klein nach groß
# print(preise)

# preise.reverse()        # --> Sortiert die Liste von groß nach klein
# print(preise)

# ==============================================================================

# Aufgabe 1:
 
# Sie haben eine Liste mit den gemessenen Temperaturen einer Woche vorliegen:
# temperaturen = [18, 22, 15, 26, 19, 21, 17]
# Schreiben Sie ein Python-Programm, das diese Liste durchläuft.
# Zählen Sie, wie viele Tage eine Temperatur von über 20 Grad hatten.

# Lösung

# temperaturen = [18, 22, 15, 26, 19, 21, 17]
# zähler = 0

# for i in temperaturen:
#     if i >20:
#         zähler += 1
# print(f"Es waren insgesamt {zähler} Tage über 20°")

# a = []      # --> So wandelt man int in float um
# for i in temperaturen:
#     a.apennd(float(i))

# ==============================================================================