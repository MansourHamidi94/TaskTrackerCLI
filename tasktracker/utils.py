# Utility functions for loading/saving tasks

import json

def load_tasks(file_path="tasks.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, file_path="tasks.json"):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)
