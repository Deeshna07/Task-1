def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_menu():
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == '2':
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks, filename)
                print("Task added!")
            else:
                print("Empty task cannot be added.")

        elif choice == '3':
            if not tasks:
                print("No tasks to remove.")
                continue

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks, filename)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option! Please choose between 1-4.")

if __name__ == "__main__":
    main()
