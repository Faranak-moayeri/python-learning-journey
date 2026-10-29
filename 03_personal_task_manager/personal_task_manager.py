"""
Personal Task Manager Project
Author: Faranak Moayeri
Description: A beginner-friendly Python program to manage daily tasks using lists.
"""

tasks = []

while True:
    print("\n===== Personal Task Manager =====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

    # Read user choice and remove extra whitespace
    choice = input("\nChoose an option: ").strip()

    # Option 1: View tasks
    if choice == "1":
        if not tasks:
            print("\n⚠️  Your task list is empty.")
        else:
            print("\n📋 My Tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

        input("\nPress Enter to return to the menu...")

    # Option 2: Add a task
    elif choice == "2":
        task = input("\nEnter a new task: ")
        if task.strip():
            tasks.append(task.strip())
            print("✅ Task added successfully!")
        else:
            print("⚠️ Task cannot be empty.")

        input("\nPress Enter to return to the menu...")

    # Option 3: Delete a task
    elif choice == "3":
        if not tasks:
            print("\n⚠️ There are no tasks to delete.")
        else:
            print("\n📋 My Tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                raw_num = input("\nEnter the task number to delete: ").strip()
                number = int(raw_num)

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"🗑️ Deleted: {deleted_task}")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        input("\nPress Enter to return to the menu...")

    # Option 4: Exit program
    elif choice == "4":
        print("\nGoodbye! Have a productive day! 👋")
        break

    # Invalid input
    else:
        print("\n⚠️ Invalid option. Please choose between 1 and 4.")
        input("\nPress Enter to return to the menu...")
