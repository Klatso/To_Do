class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def set_completed(self, status):
        self.is_completed = status


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
        # aufgabe nicht gefunden

    def edit_task(self, name, changed_attribute):
        for task in self.tasks:
            if task.name == name:
                if changed_attribute == "name":
                    # task.name = input("Gib den neuen Namen ein!")
                    # name geändert
                    pass
                elif changed_attribute == "status":
                    """
                    als erledigt markieren?
                    if change_status == "j":
                        task.mark_completed()
                        #als erledigt markiert
                    elif change_status == "n":
                        task.is_completed = False
                        #als nicht erledigt markiert
                    """
                else:
                    pass
                # name nicht gefunden
                return

    def show_tasks(self):
        for task in self.tasks:
            print(str(task))
