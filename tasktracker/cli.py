import sys
from tasktracker.tasks import add_task, list_tasks, update_task, delete_task

def main():
    print("CLI started...")  # Debugging print
    print(f"Arguments received: {sys.argv}")  # Debugging print

    if len(sys.argv) < 2:
        print("Usage: python -m tasktracker.cli <command> [options]")
        return

    command = sys.argv[1]
    print(f"Command: {command}")  # Debugging print

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python -m tasktracker.cli add <description>")
        else:
            result = add_task(" ".join(sys.argv[2:]))
            print(result)
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        tasks = list_tasks(status)
        if tasks:
            for task in tasks:
                print(f"[{task['id']}] {task['description']} - {task['status']}")
        else:
            print("No tasks found.")
    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: python -m tasktracker.cli update <id> [description] [status]")
        else:
            task_id = int(sys.argv[2])
            description = sys.argv[3] if len(sys.argv) > 3 else None
            status = sys.argv[4] if len(sys.argv) > 4 else None
            result = update_task(task_id, description, status)
            print(result)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python -m tasktracker.cli delete <id>")
        else:
            task_id = int(sys.argv[2])
            result = delete_task(task_id)
            print(result)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
