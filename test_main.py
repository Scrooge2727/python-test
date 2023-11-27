import unittest
from main import Task, TaskList

class TaskTest(unittest.TestCase):
    def test_task_completion(self):
        task = Task("Buy groceries", "Milk, eggs, bread")
        self.assertFalse(task.completed)
        task.mark_as_completed()
        self.assertFalse(task.completed)

    def test_task_info(self):
        task = Task("Buy groceries", "Milk, eggs, bread")
        task_info = task.get_task_info()
        expected_info = "Title: Buy groceries\nDescription: Milk, eggs, bread\nCompleted: False"
        self.assertEqual(task_info, expected_info)

    def test_task_info2(self):
        task = Task("123", "123")
        task_info = task.get_task_info()
        expected_info = "Title: 123\nDescription: 123\nCompleted: False"
        self.assertEqual(task_info, expected_info)

    def test_task_default_completion(self):
        task = Task("Walk the dog", "Take the dog for a walk")
        self.assertFalse(task.completed)

class TaskListIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()

    def test_add_task(self):
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        self.task_list.add_task(task1)
        self.task_list.add_task(task2)

        self.assertListEqual(self.task_list.tasks, [task1, task2])

    def test_remove_task(self):
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        self.task_list.add_task(task1)
        self.task_list.add_task(task2)

        self.task_list.remove_task(task2)  # Remove an existing task
        self.assertListEqual(self.task_list.tasks, [task1])

    def test_get_all_tasks_info(self):
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        self.task_list.add_task(task1)
        self.task_list.add_task(task2)

        all_tasks_info = self.task_list.get_all_tasks_info()
        expected_info = "Tasks:\nTitle: Buy groceries\nDescription: Milk, eggs, bread\nCompleted: False\n" \
                        "Title: Complete project\nDescription: Finish the coding project\nCompleted: False"
        self.assertEqual(all_tasks_info, expected_info)

    def test_get_completed_tasks(self):
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        task1.mark_as_completed()
        self.task_list.add_task(task1)
        self.task_list.add_task(task2)

        completed_tasks = self.task_list._get_completed_tasks()
        self.assertListEqual(completed_tasks, [task1])

    def test_remove_nonexistent_task(self):
        # Test removing a task that doesn't exist in the list
        task1 = Task("Buy groceries", "Milk, eggs, bread")
        task2 = Task("Complete project", "Finish the coding project")

        self.task_list.add_task(task1)
        with self.assertRaises(ValueError):
            self.task_list.remove_task(task2)  # Attempt to remove a non-existent task


