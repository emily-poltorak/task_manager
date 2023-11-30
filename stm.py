from task import Task
from taskmanager import TaskManager

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nSimple Task Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Tasks")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task_manager.add_task()

        elif choice == "2":
            task_manager.delete_task()
        
        elif choice == "3":
           task_manager.edit_task()

        elif choice == "4":
            task_manager.view_tasks()
        

        elif choice == "5":
            print("Exited successfully. Have a great day!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
