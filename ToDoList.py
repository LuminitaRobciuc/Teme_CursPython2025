import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO DO LIST 📝")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.config(bg="#f0f0f0")

        # Listă de task-uri (fără fișiere externe)
        self.taskuri = []

        # Titlu
        tk.Label(root, text="TO DO LIST", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        # Câmp pentru adăugare task
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Buton Adaugă
        tk.Button(root, text="Adaugă task", width=20, bg="#4CAF50", fg="white",
                  command=self.adauga_task).pack(pady=5)

        # Lista de task-uri
        self.lista = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
        self.lista.pack(pady=10)

        # Butoane de acțiune
        frame_butoane = tk.Frame(root, bg="#f0f0f0")
        frame_butoane.pack(pady=10)

        tk.Button(frame_butoane, text="Marchează ca făcut", bg="#2196F3", fg="white",
                  width=18, command=self.marcheaza_fapt).grid(row=0, column=0, padx=5)
        tk.Button(frame_butoane, text="Șterge task", bg="#f44336", fg="white",
                  width=18, command=self.sterge_task).grid(row=0, column=1, padx=5)

    def adauga_task(self):
        task = self.entry.get().strip()
        if task:
            self.taskuri.append((task, False))  # (nume, status)
            self.actualizeaza_lista()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenție", "Introdu un task valid!")

    def marcheaza_fapt(self):
        selectie = self.lista.curselection()
        if selectie:
            index = selectie[0]
            task, _ = self.taskuri[index]
            self.taskuri[index] = (task, True)
            self.actualizeaza_lista()
        else:
            messagebox.showinfo("Info", "Selectează un task din listă!")

    def sterge_task(self):
        selectie = self.lista.curselection()
        if selectie:
            index = selectie[0]
            del self.taskuri[index]
            self.actualizeaza_lista()
        else:
            messagebox.showinfo("Info", "Selectează un task pentru a-l șterge!")

    def actualizeaza_lista(self):
        self.lista.delete(0, tk.END)
        for task, status in self.taskuri:
            text = f"{task} {'✅' if status else ''}"
            self.lista.insert(tk.END, text)

# Pornire aplicație
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()