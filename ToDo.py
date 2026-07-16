import json


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
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename

    def add_task(self, task):
        self.tasks.append(task)
        self.save()

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                self.save()
                return

    def rename_task(self, name, new_name):
        for task in self.tasks:
            if task.name == name:
                task.name = new_name
                self.save()
                return

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(entry) for entry in data]
        except FileNotFoundError:
            self.tasks = []
