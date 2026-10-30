# ==============================================================================

import os       # --> Bibliothek wird importiert
import platform

# print(os.getlogin())    # --> Username wird angezeigt
# # print(os.environ)       # --> Auf Umgebungsvariablen (Environment Variables) des Betriebssystems zugreifen
# print(os.getenv("USERPROFILE"))     # -->  Ausgabe: C:\Users\UserS2025
# print(os.getenv("PROCESSOR_ARCHITECTURE"))      # --> Ausgabe: AMD64
# print(os.getenv("LANG"))        # --> Ausgabe: en_US.UTF-8
# os.environ["MYVAR"] = "secret_value"        # --> Selbst eine Variable erstellen

# print(os.cpu_count())       # --> Ausgabe: 16
# print(os.listdrives())      # --> Ausgabe: ['C:\\']
# print(os.getcwd())      # --> Ausgabe: C:\Users\UserS2025\Desktop\Schule\Visual Studio
# # os.chdir("")        # Auch möglich ändert den Platz wo wir Änderungen machen wollen

# ==============================================================================

# print(os.listdir(path="."))     # --> Ausgabe als Liste: ['Aufgaben', 'Python']

# for i in os.listdir(path="../../"):
#     print(i)

# ==============================================================================

# try:
#     os.mkdir("ordner_01")       # Erstellt einen Ordner im jetzigen Verzeichnis
# except FileExistsError:
#     print("File already exists!")

# os.rename("ordner_01","ordner_02")      # Bennent den vorhandenen Ordner um

# os.rmdir("ordner_02")       # Löscht den angegebenen Ordner

# # os.remove()     # Würde eine angegebene Datei löschen

# ==============================================================================

# info = os.stat("Python/Abendlied.txt")      # --> Gibt die Stats aus
# print(info)
# print(info.st_size)
# print(oct(info.st_mode)[-3:])

# print(os.name)

# ==============================================================================

print(platform.system())        # --> Zeigt das Betriebssystem an

# ==============================================================================