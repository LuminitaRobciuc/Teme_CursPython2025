# Calculator cu 5 functii (+, -, *, %, stergere)

import tkinter as tk

# Funcția care gestionează apăsarea butoanelor
def apasa(tasta):
    if tasta == "C":
        ecran.delete(0, tk.END)  # șterge tot
    elif tasta == "=":
        try:
            expresie = ecran.get().replace("%", "/")
            rezultat = eval(expresie)  # calculează
            ecran.delete(0, tk.END)
            ecran.insert(tk.END, str(rezultat))  # afișează rezultatul
        except Exception:
            ecran.delete(0, tk.END)
            ecran.insert(tk.END, "Eroare")
    else:
        ecran.insert(tk.END, tasta)  # adaugă cifra

# Fereastra principală
root = tk.Tk()
root.title("Calculator Python (fără fișiere externe)")
root.geometry("300x400")
root.resizable(False, False)

# Afișajul calculatorului
ecran = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
ecran.pack(padx=10, pady=10, fill="x")

# Lista de butoane
butoane = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "%", "C", "="
]

# Butoane
frame = tk.Frame(root)
frame.pack()

# Creare butoane
rand = 0
coloana = 0

for b in butoane:
    buton = tk.Button(
        frame,
        text=b,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda t=b: apasa(t)
    )
    buton.grid(row=rand, column=coloana, padx=5, pady=5)

    coloana += 1
    if coloana > 3:
        coloana = 0
        rand += 1

# Pornește calculatorul
root.mainloop()