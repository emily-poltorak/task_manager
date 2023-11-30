from task import Task 
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Task name: ")
        due_date = input("Due date (MM-DD-YYYY): ")
        priority = input("Priority (High/Medium/Low): ").lower()
        new_task = Task(name, due_date, priority, "open")
        self.tasks.append(new_task)
        
        print(f"Task: '{name}' added successfully!")
                

    def delete_task(self):
        name = input("Enter the name of the task you want to delete: ")

        for i in self.tasks:
            if i.name == name:
                self.tasks.remove(i)
                print(f"Task '{name}' deleted successfully!")
                return True
            else:
                print("Task not found!")
                return False
    
    def edit_task(self):
        name = input("Enter the name of the task you would like to edit: ")
            
        for i in self.tasks:
            if i.name == name:
                make_edit = int(input("What edit would you like to change:\n Enter 1. Name\n 2. Date\n 3. Priority\n 4. State\n"))
                if make_edit == 1:
                    change_name = input("Enter the new name for the task: ")
                    i.name = change_name

                elif make_edit == 2:
                    change_date = input("Enter the new date for the task(DD-MM-YYYY): ")
                    i.due_date = change_date

                elif make_edit == 3:
                    change_priority = input("Enter the new priority for the task(High/Medium/Low): ").lower()
                    i.priority = change_priority

                elif make_edit == 4:
                    change_state = input("Have you completed this task? Y/N:  ").lower()
                    if change_state == "y":
                        i.state = 'done'
                    else:
                        pass
            break


    def view_tasks(self):
        print("\nTasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

