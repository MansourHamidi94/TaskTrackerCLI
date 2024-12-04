# Task Management Functions 
# Core functionalities: add, update, delete, list tasks

from datetime import datetime
from .utils import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    task_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return f"Task added successfully (ID: {task_id})"

def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if not status or task["status"] == status]
    return filtered_tasks

def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if description:
                task["description"] = description
            if status:
                task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            return f"Task {task_id} updated successfully"
    return f"Task with ID {task_id} not found."

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) < len(tasks):
        save_tasks(new_tasks)
        return f"Task {task_id} deleted successfully."
    return f"Task with ID {task_id} not found."
