# Step 1 Display Function

def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty. ")
    else:
        print("To-Do list: ")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


# Step 2 Adding task in todo_list

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to your todo_list.")


# Removing task function

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task index. Please enter a valid task index.")

# Step 3 implement the main function
def main():
    todo_list = []

    while True:
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task you want to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            try:
                task_index = int(input("Enter the task index you want to remove: "))
                remove_task(todo_list, task_index)
            except ValueError:
                print("Invalid input. Please enter a valid task index (integer).")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()

