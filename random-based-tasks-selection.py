import tkinter as tk
import pandas as pd
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.df = pd.read_excel('Aufgabenliste.xlsx')
        self.completed = []
        self.load_completed()

    def create_widgets(self):
        
        self.selected_task = tk.StringVar()
        self.selected_task.set("Bereit zur Auswahl einer Aufgabe.")
        self.task_label = tk.Label(self, textvariable=self.selected_task)
        self.task_label.grid(row=0, column=0, columnspan=2)

        self.select_button = tk.Button(self, text="Aufgabe auswählen", command=self.select_task)
        self.select_button.grid(row=1, column=0)

        self.restart_button = tk.Button(self, text="Neustart", command=self.restart)
        self.restart_button.grid(row=1, column=1)

    def select_task(self):
        available = [i for i in range(len(self.df)) if i not in self.completed]
        if not available:
            self.selected_task.set("Alle Aufgaben erledigt.")
            return
        selected = random.choice(available)
        self.selected_task.set(f"Übung: {self.df.iloc[selected]['Übung']}, Thema: {self.df.iloc[selected]['Thema']}, Aufgabennummer: {self.df.iloc[selected]['Aufgabennummer']}")
        self.completed.append(selected)
        self.save_completed()

    def restart(self):
        self.completed = []
        self.save_completed()
        self.selected_task.set("Bereit zur Auswahl einer Aufgabe.")

    def save_completed(self):
        with open('completed.txt', 'w') as f:
            for item in self.completed:
                f.write(f"{item}\n")

    def load_completed(self):
        try:
            with open('completed.txt', 'r') as f:
                for line in f:
                    self.completed.append(int(line.strip()))
        except FileNotFoundError:
            pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()
