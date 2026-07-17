import json
import datetime


class Task:
    def __init__(self, name, is_completed=False, time_created=None, time_completed=None):
        self.name = name
        self.is_completed = is_completed
        self.time_created = datetime.datetime.now(
        ) if time_created is None else time_created
        self.time_completed = time_completed

    def set_completed(self, status):
        self.is_completed = status
        if status:
            self.time_completed = datetime.datetime.now()
        else:
            self.time_completed = None

    def to_dict(self):
        time_created_isoformat = self.time_created.isoformat()
        self.time_completed_isoformat = self.time_completed.isoformat(
        ) if self.time_completed is not None else None
        return {"name": self.name, "is_completed": self.is_completed, "time_created": time_created_isoformat, "time_completed": self.time_completed_isoformat, }

    @staticmethod
    def from_dict(data):
        time_created_output = datetime.datetime.fromisoformat(
            data.get("time_created"))
        time_completed_output = datetime.datetime.fromisoformat(
            data.get("time_completed")) if data.get("time_completed") is not None else None
        return Task(data["name"], data["is_completed"], time_created_output, time_completed_output)


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
