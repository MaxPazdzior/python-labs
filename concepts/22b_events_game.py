# ==============================================================================

import tkinter as tk
import random

# ==============================================================================

def bewege_ziel():
    x = random.randint(20,380)
    y = random.randint(20,380)
    canvas.coords(ziel, x - 15, y - 15, x + 15, y + 15)

def treffer(event):
    aktuelle_punkte = punkte.get() +1
    punkte.set(aktuelle_punkte)
    bewege_ziel()

# ==============================================================================

# Hauptfenster erstellen
fenster = tk.Tk()
fenster.geometry("400x400")

# Tkinter-Variablen für den Spielzustand
punkte = tk.IntVar(value=0)
restzeit = tk.IntVar(value=20)

# Spielfläche erstellen (Canvas)
canvas = tk.Canvas(fenster, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)  # --> expand True bedeutet, dass man das Fenster größer ziehen kann, sodass sich das Programm mit anpasst

ziel = canvas.create_oval(185,185,215,215,fill="red")

canvas.tag_bind(ziel, "<Button-1>", treffer)

fenster.mainloop()

# ==============================================================================
