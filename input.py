from main import Task, TaskList

def create_task():
    # pragma: no cover
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    return Task(title, description)


def print_task_list(task_list):
    # pragma: no cover
    print("Tasks:")
    for index, task in enumerate(task_list.tasks, start=1):
        print(f"{index}. {task.get_task_info()}")


# Пример использования
def main():
    # pragma: no cover
    task_list = TaskList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_task = create_task()
            task_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            print_task_list(task_list)
            task_index_to_remove = input("Enter the number of the task to remove: ")
            try:
                task_to_remove = task_list.tasks[int(task_index_to_remove) - 1]
                task_list.remove_task(task_to_remove)
                print("Task removed successfully!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "3":
            print_task_list(task_list)
            task_index_to_complete = input("Enter the number of the task to mark as completed: ")
            try:
                task_to_complete = task_list.tasks[int(task_index_to_complete) - 1]
                task_to_complete.mark_as_completed()
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "4":
            print_task_list(task_list)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()