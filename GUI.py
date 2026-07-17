import tkinter as tk
import ToDo

todo = ToDo.ToDoList()

todo.load()

window = tk.Tk()
window.title("ToDo-Liste")
window.geometry("350x400")
window.configure(bg="#f0f0f0")
window.rowconfigure(1, minsize=20)

window.columnconfigure(0, weight=1)

title = tk.Label(window, text="Aufgaben", font=(
    "TkDefaultFont", 16, "bold"), bg="#f0f0f0")
title.grid(row=0, column=0)

task_field = tk.Frame(window)
task_field.grid(row=2, column=0, sticky="ew")

task_field.columnconfigure(0, weight=1)
task_field.columnconfigure(1, weight=3)
task_field.columnconfigure(2, weight=1)
task_field.configure(bg="#f0f0f0")
task_field.rowconfigure(len(todo.tasks)+1, minsize=30)

task_input = None
button_add = None
input_open = False
editing_task = None


def show_input_field():
    global task_input, input_open, editing_task
    input_open = True
    editing_task = None

    task_input = tk.Entry(task_field)
    task_input.grid(row=len(todo.tasks)+1, column=0,
                    columnspan=3, sticky="ew", padx=10)

    button_add.grid(row=len(todo.tasks)+2, column=0,
                    columnspan=3, sticky="ew", padx=10)
    button_add.config(text="✓", command=confirm_input)


def create_labels(task_object):
    global button_add

    for widget in task_field.winfo_children():
        if widget != task_input:
            widget.destroy()
    for index, obj in enumerate(task_object):
        var = tk.BooleanVar(value=obj.is_completed)
        checkbox = tk.Checkbutton(
            task_field,
            variable=var,
            bg="#f0f0f0",
            command=lambda obj=obj, var=var: (
                obj.set_completed(var.get()), todo.save(
                ), create_labels(todo.tasks),
            )
        )
        checkbox.grid(row=index, column=0)

        label_task = tk.Label(task_field, text=obj.name, bg="#f0f0f0")
        label_task.grid(row=index, column=1, sticky="w")
        label_task.bind("<Button-3>", lambda e,
                        obj=obj: show_context_menu(e, obj))

        time_string = (obj.time_created if not obj.is_completed else obj.time_completed).strftime(
            "%d.%m.%Y %H:%M")
        label_time_created_or_completed = "Erstellt:" if not obj.is_completed else "Erledigt:"
        label_time = tk.Label(
            task_field, text=f"{label_time_created_or_completed} {time_string}", font=("TkDefaultFont", 8), bg="#f0f0f0")
        label_time.grid(row=index, column=2, sticky="w")

    button_add = tk.Button(task_field, text="+",
                           borderwidth=1, relief="flat", highlightthickness=1, highlightbackground="#888888",
                           bg="#f0f0f0", activebackground="#e0e0e0",  command=show_input_field)

    button_row = len(task_object) + 1

    if input_open:
        button_row += 1

    task_field.rowconfigure(len(task_object), minsize=15)

    button_add.grid(row=button_row, column=0,
                    columnspan=3, sticky="ew", padx=10)

    button_add.bind("<Enter>", lambda e: button_add.config(
        text="Aufgabe hinzufügen")if not input_open else None)
    button_add.bind("<Leave>", lambda e: button_add.config(
        text="+") if not input_open else None)


def show_context_menu(event, obj):
    menu = tk.Menu(window, tearoff=0)
    menu.add_command(label="Aufgabe umbenennen",
                     command=lambda: rename_task(obj))
    menu.add_command(label="Aufgabe entfernen",
                     command=lambda: delete_task(obj))
    menu.tk_popup(event.x_root, event.y_root)


def delete_task(obj):
    todo.delete_task(obj.name)
    create_labels(todo.tasks)


def rename_task(obj):
    global task_input, input_open, editing_task, button_add
    input_open = True
    editing_task = obj

    row = todo.tasks.index(obj)

    for widget in task_field.grid_slaves(row=row, column=1):
        widget.destroy()

    task_input = tk.Entry(task_field)
    task_input.insert(0, obj.name)
    task_input.grid(row=row, column=1, sticky="ew")
    task_input.focus()
    task_input.select_range(0, tk.END)
    task_input.bind("<Return>", lambda e: confirm_input())

    button_add.config(text="✓", command=confirm_input)


def confirm_input():
    global task_input, input_open, editing_task

    name = task_input.get()
    if name:
        if editing_task is None:
            todo.add_task(ToDo.Task(name))
        else:
            todo.rename_task(editing_task.name, name)

    task_input.destroy()
    task_input = None
    input_open = False
    editing_task = None
    create_labels(todo.tasks)


create_labels(todo.tasks)
window.mainloop()
