from .task import Task
from datetime import datetime


class TaskList:

    def __init__(self):
        self.__tasks = []

    @property
    def tasks(self):
        return self.__tasks.copy()

    def add_task(self, description, priority='medium', due_date=None):
        task = Task(description, priority, due_date)
        self.__tasks.append(task)
        return task

    def remove_task(self, index):
        if 0 <= index < len(self.__tasks):
            return self.__tasks.pop(index)
        raise IndexError("Задача с таким индексом не найдена")

    def mark_completed(self, index):
        if 0 <= index < len(self.__tasks):
            self.__tasks[index].mark_completed()
            return True
        raise IndexError("Задача с таким индексом не найдена")

    def find_by_description(self, search_text):
        search_text = search_text.lower()
        return [task for task in self.__tasks
                if search_text in task.description.lower()]

    def filter_by_priority(self, priority):
        return [task for task in self.__tasks if task.priority == priority]

    def filter_by_date(self, date_str):
        try:
            filter_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return [task for task in self.__tasks
                    if task.due_date and task.due_date.date() == filter_date]
        except ValueError:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")

    def get_pending_tasks(self):
        return [task for task in self.__tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.__tasks if task.completed]

    def sort_by_priority(self, reverse=False):
        priority_order = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
        self.__tasks.sort(
            key=lambda t: priority_order[t.priority],
            reverse=reverse
        )

    def sort_by_date(self, reverse=False):
        self.__tasks.sort(
            key=lambda t: t.due_date or datetime.max,
            reverse=reverse
        )

    def sort_by_created(self, reverse=False):
        self.__tasks.sort(key=lambda t: t.created_at, reverse=reverse)

    def __len__(self):
        return len(self.__tasks)

    def __getitem__(self, index):
        return self.__tasks[index]

    def __str__(self):
        if not self.__tasks:
            return "Список задач пуст"

        lines = ["Список задач:"]
        for i, task in enumerate(self.__tasks, 1):
            lines.append(f"{i}. {task}")
        return "\n".join(lines)
