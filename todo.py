import os
TASKS_FILE = "tasks.txt"
def load_tasks():
    """Read tasks from the text file into a list."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    return tasks


def save_tasks(tasks):
    """Write the current list of tasks back to the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks with their index numbers."""
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"  {index}. {task}")
    print()


def add_task(tasks):
    """Add a new task to the list."""
    new_task = input("Enter the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Added: '{new_task}'\n")
    else:
        print("Task cannot be empty.\n")


def remove_task(tasks):
    """Remove a task from the list by its number."""
    view_tasks(tasks)
    if not tasks:
        return
    choice = input("Enter the task number to remove: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        removed = tasks.pop(int(choice) - 1)
        save_tasks(tasks)
        print(f"Removed: '{removed}'\n")
    else:
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    menu = """
====== TO-DO LIST APP ======
1. View tasks
2. Add task
3. Remove task
4. Exit
=============================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()