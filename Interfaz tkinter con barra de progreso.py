import tkinter as tk
from tkinter import ttk
import time

def iniciar_progreso():
    """Simula el progreso de una tarea."""
    for i in range(101):
        barra_progreso['value'] = i
        ventana.update_idletasks()
        time.sleep(0.05)
    messagebox.showinfo("Tarea completada", "La tarea se completó con éxito!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Barra de progreso")
ventana.geometry("400x150")

# Etiqueta
label = tk.Label(ventana, text="Progreso de la tarea:")
label.pack(pady=10)

# Barra de progreso
barra_progreso = ttk.Progressbar(ventana, length=300, mode='determinate')
barra_progreso.pack(pady=20)

# Botón para iniciar el progreso
boton_iniciar = tk.Button(ventana, text="Iniciar tarea", command=iniciar_progreso)
boton_iniciar.pack(pady=10)

# Ejecutar la interfaz
ventana.mainloop()
