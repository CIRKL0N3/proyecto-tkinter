import tkinter as tk
from tkinter import messagebox, font

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("450x500")
root.config(bg="#f0f0f0")  # Fondo claro para la ventana
root.resizable(True, True)

# Fuente personalizada
fuente = font.Font(family="Helvetica", size=12)

# Función para agregar tareas a la lista
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea")

# Función para eliminar tareas seleccionadas de la lista
def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        lista_tareas.delete(seleccion)
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

# Función para marcar tareas como completadas
def completar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        tarea = lista_tareas.get(seleccion)
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, f"[Completada] {tarea}")
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

# Frame para agrupar entrada y botones
frame_entrada = tk.Frame(root, bg="#f0f0f0")
frame_entrada.pack(pady=10)

entrada_tarea = tk.Entry(frame_entrada, width=30, font=fuente)
entrada_tarea.grid(row=0, column=0, padx=5, pady=5)

btn_agregar = tk.Button(frame_entrada, text="Agregar Tarea", command=agregar_tarea, bg="#4CAF50", fg="white", font=fuente)
btn_agregar.grid(row=0, column=1, padx=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root, bg="#f0f0f0")
frame_botones.pack(pady=10)

btn_completar = tk.Button(frame_botones, text="Completar Tarea", command=completar_tarea, bg="#008CBA", fg="white", font=fuente)
btn_completar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea, bg="#f44336", fg="white", font=fuente)
btn_eliminar.grid(row=0, column=1, padx=5)

# Frame para la lista de tareas y scrollbar
frame_lista = tk.Frame(root, bg="#f0f0f0")
frame_lista.pack(pady=10)

# Scrollbar y Listbox
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tareas = tk.Listbox(frame_lista, width=50, height=15, font=fuente, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE, bg="white", fg="black")
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
scrollbar.config(command=lista_tareas.yview)

root.mainloop()
