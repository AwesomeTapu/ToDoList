import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    title = input("Enter task name: ")
    tasks.append({"title": title, "done": False})

def mark_done(tasks):
    show_tasks(tasks)
    i = int(input("Enter task number to mark done: ")) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True

def delete_task(tasks):
    show_tasks(tasks)
    i = int(input("Enter task number to delete: ")) - 1
    if 0 <= i < len(tasks):
        tasks.pop(i)

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks\n2. Add Task\n3. Mark Task Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
