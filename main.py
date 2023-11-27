class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def get_task_info(self):
        return f"Title: {self.title}\nDescription: {self.description}\nCompleted: {self.completed}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks_info(self):
        task_info = "\n".join(task.get_task_info() for task in self.tasks)
        return f"Tasks:\n{task_info}"

    def _get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]
