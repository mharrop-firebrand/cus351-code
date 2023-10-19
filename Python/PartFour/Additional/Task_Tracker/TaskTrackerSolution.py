"""Create a simple task tracker application using Python that allows users to add, view, and mark tasks as completed.

Could look something like this: 
Task Tracker Menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Exit

"""

tasks = []


def add_task(task):
    tasks.append(task)


def view_tasks():
    if not tasks:
        print("No tasks found. Add some tasks first.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def mark_completed(task_index):
    if 1 <= task_index <= len(tasks):
        print(f"\nBefore marking as completed:")
        view_tasks()

        completed_task = tasks.pop(task_index - 1)
        print(f"\nTask '{completed_task}' marked as completed.")

        print(f"\nAfter marking as completed:")
        view_tasks() if tasks else print("All tasks complete.")
    else:
        print("Invalid task index.")


while True:
    print("\nTask Tracker Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task index to mark as completed: "))
        mark_completed(task_index)
    elif choice == "4":
        print("Exiting Task Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
