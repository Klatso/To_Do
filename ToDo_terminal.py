class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        text_status = "erledigt" if self.is_completed else "nicht erledigt"
        return (f"\n{self.name} - {text_status}")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)

                return
        print(
            f"\nDie Aufgabe {name} wurde nicht gefunden und kann nicht gelöscht werden!")

    def mark_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_completed()
                return
        print(
            f"\nDie Aufgabe {name} wurde nicht gefunden und kann nicht als erledigt markiert werden!")

    def edit_task(self, name, changed_attribute):
        for task in self.tasks:
            if task.name == name:
                if changed_attribute == "name":
                    task.name = input("Gib den neuen Namen ein!")
                    print(
                        f'\nDie Aufgabe "{name}" wurde zu "{task.name}" geändert!')
                elif changed_attribute == "status":
                    change_status = input(
                        "\nAls erledigt markieren(j/N)").lower()
                    if change_status == "j":
                        task.mark_completed()
                        print(
                            f'\nDie Aufgabe "{name}" wurde als erledigt markiert!')
                    elif change_status == "n":
                        task.is_completed = False
                        print(
                            f'\nDie Aufgabe "{name}" wurde als nicht erledigt markiert!')
                else:
                    print(
                        f"\nDas Attribut {changed_attribute} wurde nicht gefunden!")
                return
        print(
            f"\nDie Aufgabe {name} wurde nicht gefunden und kann nicht bearbeitet werden!")

    def show_tasks(self):
        for task in self.tasks:
            print(str(task))


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo Liste ---")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe erledigt")
        print("4. Aufgabe bearbeiten")
        print("5. Aufgabe löschen")
        print("6. beenden")

        choice = input("\nGib die Nummer der gewünschten Aufgabe ein!")

        if choice == "1":
            print("\nAufgabe hinzufügen!")
            name = input("Gib den Namen der neuen Aufgabe ein!")
            task = Task(name)
            todo.add_task(task)
            print(f'\nDie Aufgabe "{name}" wurde hinzugefügt')

        elif choice == "2":
            print("\nAufgaben anzeigen!")
            todo.show_tasks()

        elif choice == "3":
            print("\nAufgabe als erledigt markieren!")
            name = input("Gib den Namen der erledigten Aufgabe ein! ")
            todo.mark_completed(name)
            print(f"\nDie Aufgabe {name} wurde als erledigt markiert!")

        elif choice == "4":
            print("\nAufgabe bearbeiten!")
            name = input("Gib den Namen der zu bearbeitenden Aufgabe ein! ")
            changed_attribute = input(
                "Was soll bearbeitet werden?(Name/Status)").lower().strip()
            todo.edit_task(name, changed_attribute)

        elif choice == "5":
            print("\nAufgabe löschen")
            name = input("Gib den Namen der zu löschenden Aufgabe ein! ")
            todo.delete_task(name)

        elif choice == "6":
            print("\nProgramm beendet")
            break

        else:
            print("\nUngültige Eingabe")

    main()
