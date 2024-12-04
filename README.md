# Documentation for the code

# TaskTrackerCLI

# TaskTrackerCLI is a simple, command-line-based task management tool that allows you to add, update, delete, and list tasks stored in a JSON file. This project demonstrates basic Python concepts, including file handling, command-line argument parsing, and modular programming.

# Features

# Add Tasks: Add new tasks with a description and a default status of todo.
# List Tasks: View all tasks, optionally filtered by status (todo, in-progress, done).
# Update Tasks: Modify task descriptions or change their status.
# Delete Tasks: Remove tasks by their ID.
# Installation
# Prerequisites
# Python 3.6 or higher installed on your system.
# A terminal (Command Prompt, PowerShell, or equivalent).
# Clone the Repository
# Navigate to the directory where you want to store the project.
# Clone the repository:
# bash
# Kopier kode
# git clone https://github.com/<MansourHamidi94>/TaskTrackerCLI.git
# cd TaskTrackerCLI
# Initialize tasks.json
# Ensure tasks.json exists in the project root.
# Initialize it with an empty array:
# json
# Kopier kode
[]
# Usage
# Run the CLI tool from the project root directory:

# bash
Kopier kode 
python -m tasktracker.cli <command> [options]
Available Commands
Add a Task

bash
Kopier kode
python -m tasktracker.cli add "Task description"
Example:

bash
Kopier kode
python -m tasktracker.cli add "Finish project documentation"
List All Tasks

bash
Kopier kode
python -m tasktracker.cli list
List Tasks by Status

bash
Kopier kode
python -m tasktracker.cli list <status>
Example:

bash
Kopier kode
python -m tasktracker.cli list todo
Update a Task

bash
Kopier kode
python -m tasktracker.cli update <id> <new description> <new status>
Example:

bash
Kopier kode
python -m tasktracker.cli update 1 "Submit final report" done
Delete a Task

bash
Kopier kode
python -m tasktracker.cli delete <id>
Example:

bash
Kopier kode
python -m tasktracker.cli delete 1
Project Structure
bash
Kopier kode
TaskTrackerCLI/
├── tasktracker/
│   ├── __init__.py       # Package marker
│   ├── cli.py            # Command-line interface logic
│   ├── tasks.py          # Task management functions
│   └── utils.py          # File operations (load/save tasks)
├── tasks.json            # Data storage for tasks
├── tests/                # Test suite (optional)
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

Contributing
Contributions are welcome! Feel free to submit a pull request or create an issue for feature requests or bugs.

https://roadmap.sh/projects/task-tracker

Author
Mansour Hamidi
Created as part of a learning project to understand Python, command-line tools, and project structure.
