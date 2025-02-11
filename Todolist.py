# A very simple to-do list program
tasks = []  # This list will store the tasks

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":  # Show tasks
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":  # Add task
        new_task = input("Enter a task: ")
        tasks.append("[ ] " + new_task)  # Add task with an empty checkbox
        print(f"Task added: {new_task}")

    elif choice == "3":  # Complete a task
        if not tasks:
            print("No tasks to complete!")
        else:
            task_number = int(input("Enter task number to complete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number] = tasks[task_number].replace("[ ]", "[✔]")  # Mark as completed
                print("Task marked as complete!")
            else:
                print("Invalid task number!")

    elif choice == "4":  # Delete a task
        if not tasks:
            print("No tasks to delete!")
        else:
            task_number = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                removed_task = tasks.pop(task_number)  # Remove task from list
                print(f"Task deleted: {removed_task}")
            else:
                print("Invalid task number!")

    elif choice == "5":  
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1-5.")