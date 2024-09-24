# A simple command-line to-do list manager

tasks = []

# Function to display all tasks
def show_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['title']} - Due: {task['due_date']} - Status: {status}")

# Function to add a task
def add_task(title, due_date):
    tasks.append({"title": title, "due_date": due_date, "completed": False})
    print(f"Task '{title}' added successfully!")

# Function to mark a task as done
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['title']}' marked as completed!")
    else:
        print("Invalid task number!")

# Function to delete a task
def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed['title']}' deleted!")
    else:
        print("Invalid task number!")

# Function to update a task
def update_task(index, new_title, new_due_date):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title
        tasks[index]["due_date"] = new_due_date
        print(f"Task '{index+1}' updated successfully!")
    else:
        print("Invalid task number!")

# Main menu for interaction
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show all tasks")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Update a task")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            due_date = input("Enter due date (e.g., 2024-09-24): ")
            add_task(title, due_date)
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            complete_task(index)
        elif choice == "4":
            index = int(input("Enter task number to update: ")) - 1
            new_title = input("Enter new task title: ")
            new_due_date = input("Enter new due date: ")
            update_task(index, new_title, new_due_date)
        elif choice == "5":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
