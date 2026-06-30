 To-Do List 
## Objective
Implement a simple console-based to-do list manager that lets users add, remove, and view tasks, with the task list saved persistently to a text file.

## Tools Used
- Python 3
- VS Code / Terminal

## Key Concepts
- File Handling (`open()`, `with` statement)
- Lists
- String Manipulation (`.strip()`)

## Files
- `todo.py` — main application code
- `tasks.txt` — auto-generated file where tasks are stored (created when you run the app)

## How It Works
1. On startup, the app loads any existing tasks from `tasks.txt`.
2. A menu lets the user:
   - View all tasks
   - Add a new task
   - Remove a task by number
   - Exit
3. Every add/remove operation immediately saves the updated list back to `tasks.txt`, so tasks persist between runs.

## How to Run
```bash
python todo.py
```

## Sample Run
```
====== TO-DO LIST APP ======
1. View tasks
2. Add task
3. Remove task
4. Exit
=============================

Choose an option (1-4): 2
Enter the new task: Buy groceries
Added: 'Buy groceries'
```

## What I Learned
- How to read/write files using `open()` and the `with` statement (context managers)
- Looping through file content line by line
- Using `.strip()` to clean up input/output strings
- Using lists with `append()`, `pop()`, and `enumerate()` to manage and display data
- Handling invalid user input gracefully
-
