from datetime import datetime

class Task:

    priority_levels = {
        'low': 1,
        'medium': 2,
        'high': 3,
        'critical': 4
    }

    def __init__(self, description, priority='medium', due_date=None):
        self.__description = description
        self.__priority = self._validate_priority(priority)
        self.__due_date = self._validate_date(due_date)
        self.__completed = False
        self.__created_at = datetime.now()

    @property
    def description(self):
        return self.__description

    @property
    def priority(self):
        return self.__priority

    @property
    def due_date(self):
        return self.__due_date

    @property
    def completed(self):
        return self.__completed

    @property
    def created_at(self):
        return self.__created_at

    def _validate_priority(self, priority):
        if priority not in self.priority_levels:
            valid = ', '.join(self.priority_levels.keys())
            raise ValueError(f"Приоритет должен быть одним из: {valid}")
        return priority

    def _validate_date(self, date_str):
        if not date_str:
            return None
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")

    def mark_completed(self):
        self.__completed = True

    def __str__(self):
        status = "(выполнено)" if self.__completed else "(не выполнено)"

        priority_text = {
            'low': 'низкий',
            'medium': 'средний',
            'high': 'высокий',
            'critical': 'критический'
        }.get(self.__priority, 'средний')

        date_text = f" (срок: {self.__due_date.strftime('%d.%m.%Y')})" if self.__due_date else ""
        return f"{self.__description} | приоритет: {priority_text} | {status}{date_text}"

    def __repr__(self):
        return f"Task('{self.__description}', priority='{self.__priority}')"
