# ==============================================================================

import tkinter as tk    # --> Toolkit Interface

# Plattformübergreifend
# Widgets: Fenster (Tk), Schaltflächen (Buttons), Beschriftungen (Label)
# Layout-Manager: pack(), grid()

# ==============================================================================

# Eventhandler:
def klick_handler(event):   # --> event muss drin sein sonst funktioniert der klick handler nicht
    aktueller_wert = zaehler.get() +1   # --> Holt den Zähler den wir unten Definiert haben
    zaehler.set(aktueller_wert)
    label.config(text=f"Der Button wurde {aktueller_wert} mal geklickt!")   # --> Wird angezeigt wenn der Button gedrückt wurde

fenster = tk.Tk()
fenster.title("Eventhandler-Übung") # --> Zeigt den Titel oben im Fenster an
fenster.geometry("300x250") # --> Gibt die Größe des Fensters an

zaehler = tk.IntVar(value=0)   # --> Dient als Zähler / value=0 bedeutet, er startet bei 0

# Widgets erstellen
label = tk.Label(fenster, text="Der Button wurde noch nicht geklickt.", pady=20) # --> Wird im Fenster angezeigt / pady ist der Abstand zwischen Label und Button
button = tk.Button(fenster, text="klick mich")  # --> Button wird erstellt

# Widgets im Fenster anordnen
label.pack()    # --> Muss man machen damit es aktiviert ist
button.pack()   # --> Muss man machen damit es aktiviert ist

# Registrierung: Eventhandler an den Button binden
button.bind("<Button-1>", klick_handler)    # --> Muss nach den erstellten Widgets gemacht werden / Button 1 = Mauszeiger Links / klick_hanlder ist unsere Funktion von oben

# Endlosschleife, Eventlistener
fenster.mainloop()  # --> Endlosschleife die dafür sorgt, dass das Fenster dauerhaft offen bleibt

# ==============================================================================
