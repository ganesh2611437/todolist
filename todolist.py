import json
import datetime

# Function to load existing tasks from a file
def load_tasks():
    try:
        # Open the tasks.json file in read mode
        with open('tasks.json', 'r') as file:
            # Load and return the tasks from the file
            return json.load(file)
    except FileNotFoundError:
        # If tasks.json doesn't exist, return an empty list
        return []

# Function to save tasks to a file
def save_tasks():
    # Open the tasks.json file in write mode
    with open('tasks.json', 'w') as file:
        # Write the tasks to the file in JSON format
        json.dump(tasks, file)

# Load tasks at the beginning
tasks = load_tasks()

# Function to add a new task
def add(new_item, priority='Low', due_date=None):
    # Convert the string due date to a date object
    if due_date:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    # Add the new task to the list with its priority and due date
    tasks.append({'task': new_item, 'priority': priority, 'due_date': due_date, 'completed': False})
    print("Added Task Successfully!!\n")

# Function to mark a task as completed
def mark_complete(ind):
    # Set the task's 'completed' status to True
    tasks[ind-1]['completed'] = True
    print("Marked as completed!\n")

# Function to delete a task
def delete(ind):
    # Remove the task at the given index
    tasks.pop(ind-1)
    print("Removed Task Successfully!!\n")

# Function to show all tasks
def show():
    # Check if there are any tasks to show
    if not tasks:
        print("No Tasks to show\n")
    else:
        # Iterate over the tasks and display them with their details
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} - Priority: {task['priority']} - Due: {task['due_date']} - Completed: {task['completed']}")

# Function to update an existing task
def update(ind):
    # Get the task at the specified index
    task = tasks[ind-1]['task']
    # Prompt the user to enter a new priority and due date, or keep the existing ones
    priority = input(f"Current priority of '{task}' is {tasks[ind-1]['priority']}. Enter new priority (High, Medium, Low) or press enter to keep current: ")
    due_date = input(f"Current due date of '{task}' is {tasks[ind-1]['due_date']}. Enter new due date (YYYY-MM-DD) or press enter to keep current: ")
    if priority:
        tasks[ind-1]['priority'] = priority
    if due_date:
        tasks[ind-1]['due_date'] = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    print("Updated Task Successfully!!\n")

# Function to show overdue tasks
def show_overdue():
    print("Overdue tasks:")
    # Iterate over the tasks and check if they are overdue
    for task in tasks:
        if task['due_date'] and datetime.datetime.strptime(task['due_date'], "%Y-%m-%d").date() < datetime.date.today():
            print(task['task'])

# Function to search for a task by keyword
def search_task(query):
    # Find all tasks that contain the query string
    found_tasks = [task for task in tasks if query.lower() in task['task'].lower()]
    # Display the found tasks
    for task in found_tasks:
        print(f"{task['task']} - Priority: {task['priority']} - Due: {task['due_date']} - Completed: {task['completed']}")

# Main program function
def main():
    # Display a welcome message
    print("\n\n\t\t\tby @GANESH KODIHALLI")
    print("________________________________________")
    print("\n\t\t\t***TO DO LIST APP***\n")
    while True:
        # Display the menu of options
        print("1.ADD")
        print("2.DELETE")
        print("3.VIEW")
        print("4.UPDATE")
        print("5.MARK AS COMPLETED")
        print("6.VIEW OVERDUE TASKS")
        print("7.SEARCH TASKS")
        print("8.SAVE & EXIT")
        
        # Prompt the user to make a choice
        choice = int(input("Enter your choice: "))
        print("\n")

        # Handle the user's choice
        if choice == 1:
            # Add a new task
            
            item = input("Enter the task you want to add: ")
            priority = input("Set the priority (High, Medium, Low): ")
            due_date = input("Enter the due date (YYYY-MM-DD) or press enter for none: ")
            add(item, priority, due_date)

        elif choice == 2:
            # Delete an existing task
            if tasks:
                show()
                index = int(input("Enter the index of the task you want to delete: "))
                delete(index)
            else:
                print("No Tasks to remove\n")

        elif choice == 3:
            # Show all tasks
            show()

        elif choice == 4:
            # Update an existing task
            show()
            index = int(input("Enter the index of the task you want to update: "))
            update(index)

        elif choice == 5:
            # Mark a task as completed
            show()
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_complete(index)

        elif choice == 6:
            # Show overdue tasks
            show_overdue()

        elif choice == 7:
            # Search for tasks by a keyword
            query = input("Enter keyword to search for tasks: ")
            search_task(query)

        elif choice == 8:
            # Save all tasks to the file and exit the program
            save_tasks()
            print("Tasks saved. Exiting the program.\n")
            break

        else:
            print("Invalid choice, please try again.\n")

# Run the program if this file is executed as a script
if __name__ == "__main__":
    main()
