tasks=[]
def show_menu():
    print("\n-- To Do List menu---")
    print("1.Add Task")
    print("2.view Tasks")
    print("3.Mark Task as Done")
    print("4.Delete Task")
    print("5.Exit")
def add_task():
    task=input("Enter a new task: ") 
    tasks.append({"task": task, "done":False})
    print("\u2705 Task added") 
def view_tasks():
    if not tasks:
        print("No task in the list.")
        return 
    print("\n your tasks:")
    for i,task in enumerate(tasks):
        status="\u2705" if task["done"] else "\u274C"
        print(f"{i+1}. {task['task']} [{status}]")
def mark_done():
    veiw_tasks()
    try:
        task_no=int(input("enter task num to mark as done: "))
        tasks[task_no - 1]["done"]= True 
        print("\u2705 Task marked as done.")
    except (ValueError,IndexError):
        print("Inavalid task number")
def delete_task():
    veiw_tasks()
    try:
        task_no=int(input("enter task num for delete: "))
        removed=tasks.pop(task_no - 1)
        print(f"Deleted: {removed['task']}")
    except (ValueError,IndexError):
        print("Invalid task number") 
while True:
    show_menu()
    choice=input("choose an option (1-5): ")
    if choice=='1':
        add_task()
    elif choice=='2':
        view_tasks()
    elif choice=='3':
        mark_done()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("exiting")
        break
    else:
        print("Invalid option")                                   
