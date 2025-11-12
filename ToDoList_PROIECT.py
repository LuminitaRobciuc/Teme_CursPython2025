# ===============================================================
#                    APLICAȚIE TODO LIST - PYTHON
# ===============================================================
# Aceasta este o aplicație
# care ajută la gestionarea sarcinilor zilnice.
#
#
#   ✅ adăuga o sarcină nouă
#   ✅ vizualizare lista de sarcini
#   ✅ marcheaza o sarcină ca finalizată
#   ✅ șterge o sarcină
#   ✅ salveaza automat sarcinile într-un fișier (tasks.txt)
#
#

import os  # importăm modulul os – îl folosim ca să verifice dacă fișierul există

# ===============================================================
#Funcționalitățile aplicației:
# adăugare, vizualizare, ștergere, marcare și salvare a sarcinilor.
# ===============================================================
class ToDoList:
    def __init__(self, filename="tasks.txt"):
        """
        Constructorul clasei.
        - self.filename: numele fișierului unde salvăm sarcinile
        - self.tasks: lista în care stocăm sarcinile sub formă de dicționare
        """
        self.filename = filename
        self.tasks = []  # inițial lista e goală
        self.load_tasks()  # încărcăm sarcinile din fișier (dacă există deja)

    def add_task(self, task):
        """
        Adaugă o sarcină nouă în listă.
        Fiecare sarcină este un dicționar cu:
        - 'task': textul sarcinii
        - 'done': False (înseamnă că sarcina nu e finalizată încă)
        """
        self.tasks.append({"task": task, "done": False})
        print(f"Sarcina '{task}' a fost adăugată cu succes!")
        self.save_tasks()  # după adăugare, salvăm lista actualizată

    def view_tasks(self):
        """
        Afișează toate sarcinile din listă.
        Dacă nu există sarcini, afișează un mesaj corespunzător.
        """
        if not self.tasks:  # dacă lista e goală
            print("Nu există sarcini momentan.")
            return

        print("\n--- LISTA DE SARCINI ---")
        # Parcurgem fiecare sarcină și afișăm numărul, textul și statusul
        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"  # emoji pentru stare
            print(f"{index}. {task['task']} [{status}]")
        print("------------------------")

    def mark_done(self, index):
        """
        Marchează o sarcină ca finalizată (done=True).
        Parametru: index – numărul sarcinii din listă (începe de la 1).
        """
        try:
            self.tasks[index - 1]["done"] = True
            print(f"Sarcina '{self.tasks[index - 1]['task']}' a fost marcată ca finalizată! ✅")
            self.save_tasks()  # salveaza modificarea în fișier
        except IndexError:
            print("Index invalid! Verifică numărul sarcinii și încearcă din nou.")

    def delete_task(self, index):
        """
        Șterge o sarcină din listă, după indexul ales.
        """
        try:
            removed_task = self.tasks.pop(index - 1)  # eliminăm sarcina din listă
            print(f"Sarcina '{removed_task['task']}' a fost ștearsă! 🗑️")
            self.save_tasks()
        except IndexError:
            print("Index invalid! Încearcă din nou.")

    def save_tasks(self):
        """
        Salvează toate sarcinile într-un fișier text.
        Formatul fiecărei linii din fișier este:
        nume_sarcină|stare(True/False)
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            for task in self.tasks:
                line = f"{task['task']}|{task['done']}\n"
                file.write(line)

    def load_tasks(self):
        """
        Încarcă sarcinile salvate din fișierul tasks.txt, dacă există.
        Fiecare linie este despărțită după caracterul '|' pentru a obține:
        - numele sarcinii
        - starea (True/False)
        """
        if not os.path.exists(self.filename):  # dacă fișierul nu există, ieșim
            return
        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                task, done = line.strip().split("|")
                # convertire text 'True' în valoarea booleană True
                self.tasks.append({"task": task, "done": done == "True"})


# ===============================================================
# FUNCȚIA PRINCIPALĂ - MENIUL
# Afișeaza un meniu interactiv în consolă, iar utilizatorul
# introduce o opțiune (1-5) pentru a executa o acțiune.
# ===============================================================
def main():
    todo = ToDoList()  # creaza o instanță a clasei ToDoList

    # Buclă infinită - rulează până aleg opțiunea 5 (ieșire)
    while True:
        print("\n=== MENIU TO-DO LIST ===")
        print("1. Adaugă sarcină")
        print("2. Afișează sarcini")
        print("3. Marchează sarcină ca finalizată")
        print("4. Șterge sarcină")
        print("5. Ieșire")
        print("=========================")

        alegere = input("Alege o opțiune (1-5): ")

        # În funcție de alegere, apelez metoda corespunzătoare
        if alegere == "1":
            task = input("Scrie sarcina de adăugat: ")
            todo.add_task(task)
        elif alegere == "2":
            todo.view_tasks()
        elif alegere == "3":
            todo.view_tasks()
            index = int(input("Introdu numărul sarcinii de marcat: "))
            todo.mark_done(index)
        elif alegere == "4":
            todo.view_tasks()
            index = int(input("Introdu numărul sarcinii de șters: "))
            todo.delete_task(index)
        elif alegere == "5":
            print("La revedere! 👋 Aplicația se va închide.")
            break  # ieșire din bucla while
        else:
            print("Opțiune invalidă! Te rog să introduci un număr între 1 și 5.")


# ===============================================================
# Această condiție asigură că funcția main() se execută
# doar dacă fișierul este rulat direct (nu importat ca modul).
# ===============================================================
if __name__ == "__main__":
    main()

