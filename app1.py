# app1.py(tod_app)
import json
import os
from random import choice

TASK_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {status} {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n[1] Show Tasks [2] Add Task [3] Mark Done [4] Delete Task [5] Exit")
        choice = input("Select: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("Task Title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Task number to mark done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)

        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                del tasks[idx]
                save_tasks(tasks)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid input. Try again.")


if __name__ == "__main__":
    main()

# print("Hello from todo_db")
