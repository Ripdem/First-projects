user_choice = -1

task = []
task.append("something")

def show_list():
    print(task)

def add_task():
    task.append(input("Write content of task: "))


while user_choice != 5:
    if user_choice == 1:
        show_list()
    
    if user_choice == 2:
        add_task()
    
    print()
    print("1. Show task")
    print("2. Add task")
    print("3. Remove task")
    print("4. Save task to file")
    print("5. Quit")
    user_choice = int(input("enter the content: "))
    

