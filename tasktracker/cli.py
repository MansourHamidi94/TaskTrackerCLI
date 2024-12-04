# Command-Line Interface

import sys
from .tasks import add_task, list_tasks, update_task, delete_task

def main():
    if len(sys.argv) < 2:
        print("Usage: tasktracker <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: tasktracker add <description>")
        else:
            print(add_task(" ".join(sys.argv[2:])))
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        tasks = list_tasks(status)
        for task in tasks:
            print(f"[{task['id']}] {task['description']} - {task['status']}")
    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: tasktracker update <id> [description] [status]")
        else:
            task_id = int(sys.argv[2])
            description = sys.argv[3] if len(sys.argv) > 3 else None
            status = sys.argv[4] if len(sys.argv) > 4 else None
            print(update_task(task_id, description, status))
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: tasktracker delete <id>")
        else:
            print(delete_task(int(sys.argv[2])))
    else:
        print(f"Unknown command: {command}")
