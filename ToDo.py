class Task:
    def __init__(self, name, is_completed=False):
        self.name = name
        self.is_completed = is_completed

    def set_completed(self, status):
        self.is_completed = status

    def to_dict(self):
        return {"name": self.name, "is_completed": self.is_completed}

    @staticmethod
    def from_dict(data):
        return Task(data["name"], data["is_completed"])


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

    def rename_task(self, name, new_name):
        for task in self.tasks:
            if task.name == name:
                task.name = new_name
                return

    def show_tasks(self):
        for task in self.tasks:
            print(str(task))
