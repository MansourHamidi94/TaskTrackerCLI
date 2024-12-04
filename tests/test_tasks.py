# Unit tests for task functions

import unittest
from tasktracker.tasks import add_task, list_tasks

class TestTasks(unittest.TestCase):
    def test_add_task(self):
        description = "Test task"
        result = add_task(description)
        self.assertIn("Task added successfully", result)
        tasks = list_tasks()
        self.assertEqual(tasks[-1]["description"], description)

if __name__ == "__main__":
    unittest.main()
