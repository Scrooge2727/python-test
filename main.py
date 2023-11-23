class Task:
    def __init__(self, title, description):
        """
        Инициализация задачи.

        :param title: Заголовок задачи.
        :param description: Описание задачи.
        """
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        """
        Отметить задачу как выполненную.
        """
        self.completed = True

    def get_task_info(self):
        """
        Получить информацию о задаче.

        :return: Строка с информацией о задаче.
        """
        return f"Title: {self.title}\nDescription: {self.description}\nCompleted: {self.completed}"


class TaskList:
    def __init__(self):
        """
        Инициализация списка задач.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Добавить задачу в список.

        :param task: Экземпляр задачи.
        """
        self.tasks.append(task)

    def remove_task(self, task):
        """
        Удалить задачу из списка.

        :param task: Экземпляр задачи.
        """
        self.tasks.remove(task)

    def get_all_tasks_info(self):
        """
        Получить информацию о всех задачах в списке.

        :return: Строка с информацией о всех задачах.
        """
        task_info = "\n".join(task.get_task_info() for task in self.tasks)
        return f"Tasks:\n{task_info}"

    # Пример защищенного (protected) метода
    def _get_completed_tasks(self):
        """
        Получить список выполненных задач.

        :return: Список выполненных задач.
        """
        return [task for task in self.tasks if task.completed]


# Пример использования

# Создаем задачи
task1 = Task("Buy groceries", "Milk, eggs, bread")
task2 = Task("Complete project", "Finish the coding project")

# Создаем список задач
task_list = TaskList()

# Добавляем задачи в список
task_list.add_task(task1)
task_list.add_task(task2)

# Выводим информацию о всех задачах
print("All Tasks:")
print(task_list.get_all_tasks_info())

# Меняем статус выполнения задачи
task1.mark_as_completed()

# Выводим информацию о выполненных задачах (пример защищенного метода)
completed_tasks = task_list._get_completed_tasks()
print("\nCompleted Tasks:")
print("\n".join(task.get_task_info() for task in completed_tasks))
