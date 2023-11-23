import unittest
from main import Task, TaskList

class TaskTest(unittest.TestCase):
    def test_task_completion(self):
        # Тестирование отметки задачи как выполненной
        task = Task("Buy groceries", "Milk, eggs, bread")
        self.assertFalse(task.completed)
        task.mark_as_completed()
        self.assertTrue(task.completed)   

    def test_task_info(self):
        # Тестирование получения информации о задаче
        task = Task("Buy groceries", "Milk, eggs, bread")
        task_info = task.get_task_info()
        expected_info = "Title: Buy groceries\nDescription: Milk, eggs, bread\nCompleted: False"
        self.assertEqual(task_info, expected_info)

    def test_task_default_completion(self):
        # Тестирование, что новая задача по умолчанию не выполнена
        task = Task("Walk the dog", "Take the dog for a walk")
        self.assertFalse(task.completed)

class TaskListIntegrationTest(unittest.TestCase):
    def test_add_remove_task(self):
        # Тестирование добавления и удаления задач из списка
        task_list = TaskList()
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        task_list.add_task(task1)
        task_list.add_task(task2)

        self.assertEqual(len(task_list.tasks), 2)

        task_list.remove_task(task1)
        self.assertEqual(len(task_list.tasks), 1)
        self.assertEqual(task_list.tasks[0], task2)

    def test_get_all_tasks_info(self):
        # Тестирование получения информации о всех задачах в списке
        task_list = TaskList()
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        task_list.add_task(task1)
        task_list.add_task(task2)

        all_tasks_info = task_list.get_all_tasks_info()
        expected_info = "Tasks:\nTitle: Buy groceries\nDescription: Milk, eggs, bread\nCompleted: False\n" \
                        "Title: Complete project\nDescription: Finish the coding project\nCompleted: False"
        self.assertEqual(all_tasks_info, expected_info)

if __name__ == '__main__':
    unittest.main()
