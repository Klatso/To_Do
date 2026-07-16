import tkinter as tk

window = tk.Tk()
window.title("ToDo-Liste")
window.geometry("350x400")

title = tk.Label(window, text="Aufgaben")
title.grid(row=0, column=0)

task_field = tk.Frame(window)
task_field.grid(row=1, column=0)

window.mainloop()
