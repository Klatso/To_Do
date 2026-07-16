import tkinter as tk
import ToDo

window = tk.Tk()
window.title("ToDo-Liste")
window.geometry("350x400")

window.rowconfigure(1, minsize=20)

window.columnconfigure(0, weight=1)

title = tk.Label(window, text="Aufgaben")
title.grid(row=0, column=0)

task_field = tk.Frame(window)
task_field.grid(row=2, column=0, sticky="ew")

task_field.columnconfigure(0, weight=1)
task_field.columnconfigure(1, weight=3)
task_field.columnconfigure(2, weight=1)


def create_labels(task_object):
    for index, obj in enumerate(task_object):
        var = tk.BooleanVar(value=obj.is_completed)
        checkbox = tk.Checkbutton(
            task_field,
            variable=var,
            command=lambda obj=obj, var=var: (
                obj.set_completed(var.get()),
                # print(obj.name, obj.is_completed)
            )
        )
        checkbox.grid(row=index, column=0)

        label = tk.Label(task_field, text=obj.name)
        label.grid(row=index, column=1, sticky="w")


todo = ToDo.ToDoList()

todo.add_task(ToDo.Task("Einkaufen"))
todo.add_task(ToDo.Task("Lernen"))
# zu liste hinzufügen später über GUI

create_labels(todo.tasks)
window.mainloop()
