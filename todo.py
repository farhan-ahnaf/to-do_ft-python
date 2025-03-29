import os

TODO_FILE = 'todo.txt'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            tasks = f.readlines()
        return [task.strip() for task in tasks]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        for task in tasks:
            f.write(f"{task}\n")

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def remove_task():
    show_tasks()
    try:
        task_idx = int(input("Enter the number of the task to remove: ")) - 1
        tasks = load_tasks()
        removed_task = tasks.pop(task_idx)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def mark_task_completed():
    show_tasks()
    try:
        task_idx = int(input("Enter the number of the task to mark as completed: ")) - 1
        tasks = load_tasks()
        tasks[task_idx] = tasks[task_idx] + " (Completed)"
        save_tasks(tasks)
        print(f"Task '{tasks[task_idx]}' marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        
        choice = input("Select an
