import tkinter as tk
from tkinter import messagebox
import os
import json

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("400x500")

        # Archivo para guardar las tareas
        self.file_name = "agenda_data.json"
        self.tasks = self.load_tasks()

        # Widgets de la interfaz
        self.task_input = tk.Entry(root, width=35)
        self.task_input.pack(pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Borrar Todo", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=20)
        self.task_listbox.pack(pady=10)

        self.load_listbox()

    def load_tasks(self):
        """Carga las tareas desde un archivo JSON."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Guarda las tareas en un archivo JSON."""
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_input.get().strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.save_tasks()
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def clear_tasks(self):
        """Elimina todas las tareas de la lista."""
        if messagebox.askyesno("Confirmación", "¿Estás seguro de borrar todas las tareas?"):
            self.tasks.clear()
            self.save_tasks()
            self.task_listbox.delete(0, tk.END)

    def load_listbox(self):
        """Carga las tareas en el Listbox."""
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Inicializa la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
