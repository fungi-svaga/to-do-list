from .task import Task


class PriorityManager:

    def __init__(self, task_list):
        self.task_list = task_list

    def get_priority_distribution(self):
        distribution = {p: 0 for p in Task.priority_levels.keys()}
        for task in self.task_list.tasks:
            distribution[task.priority] += 1
        return distribution

    def get_high_priority_tasks(self):
        return [task for task in self.task_list.tasks
                if task.priority in ['high', 'critical']]

    def suggest_next_task(self):
        pending = self.task_list.get_pending_tasks()
        if not pending:
            return None

        priority_order = {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}

        def task_score(task):
            score = priority_order[task.priority] * 10
            if task.due_date:
                days_left = (task.due_date - task.created_at).days
                if days_left < 0:
                    score += 5  # Просроченные задачи
                elif days_left < 2:
                    score += 3  # Срочные задачи
            return score

        return max(pending, key=task_score)

    def change_priority(self, task, new_priority):
        if new_priority not in Task.priority_levels:
            valid = ', '.join(Task.priority_levels.keys())
            raise ValueError(f"Приоритет должен быть одним из: {valid}")
        task._Task__priority = new_priority
