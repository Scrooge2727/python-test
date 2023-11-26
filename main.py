# main.py

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

def main():
    task_list = TaskList()

    while True:
        print("Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Логика для добавления задачи
            pass
        elif choice == "2":
            # Логика для удаления задачи
            pass
        elif choice == "3":
            # Логика для отметки задачи как выполненной
            pass
        elif choice == "4":
            # Логика для просмотра всех задач
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
# pragma: no cover
if __name__ == "__main__":
    main()
