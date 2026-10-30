# ==============================================================================

# Selektion, Verzweigung, Bedingte Anweisungen, IF/Else

tore_DE = 1
tore_BR = 1
k_o = False

# Erste "Stufe": IF/IF
# if tore_DE > tore_BR:
#     print("Deutschland hat gewonnen!")

# if tore_BR > tore_DE:
#     print("Brasilien hat gewonnen!")

# Zweite "Stufe": IF/ELSE
# if tore_DE > tore_BR:
#     print("Deutschland hat gewonnen!")
# else:
#     print("Brasilien hat gewonnen!")

# Dritte "Stufe": IF/ELIF/ELSE
# if tore_DE > tore_BR:
#     print("Deutschland hat gewonnen!")
# elif tore_BR > tore_DE:
#     print("Brasilien hat gewonnen!")
# else:
#     print("Unentschieden!")

# Vierte "Stufe": Verschachtelte IF/ELSE
if tore_DE > tore_BR:
    print("Deutschland hat gewonnen!")
elif tore_BR > tore_DE:
    print("Brasilien hat gewonnen!")
else:
    if k_o:
        print("Im Elfmeterschießen entscheiden!")
    else:
        print("Unentschieden!")

# ==============================================================================