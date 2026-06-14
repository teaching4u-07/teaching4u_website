# To-Do List App

tasks = []  # Empty list to store tasks

def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=========================")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = "✓" if t["done"] else "✗"
            print(f"{i}. {t['task']} [{status}]")

def complete_task():
    view_tasks()

    if tasks:
        try:
            n = int(input("Enter task number to mark complete: "))

            if 1 <= n <= len(tasks):
                tasks[n - 1]["done"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")

def delete_task():
    view_tasks()

    if tasks:
        try:
            n = int(input("Enter task number to delete: "))

            if 1 <= n <= len(tasks):
                removed = tasks.pop(n - 1)
                print(f"Deleted: {removed['task']}")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")

def main():
    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thanks for using To-Do List App!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
