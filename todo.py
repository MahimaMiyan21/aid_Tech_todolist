import pickle

tasks = []

def add_task(task):
    tasks.append(task)
    print("task added: ",task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("task removed: ",task)
    else:
        print("task not found: ",task)

def show_tasks():
    if tasks:
        print("tasks: ",tasks)
        for index, task in enumerate(tasks,start=1):
            print(f"{index}.{task}")
    else:
        print("no tasks yet.")

def save_tasks(filename):
    with open(filename,"wb") as file:
        pickle.dump(tasks,file)
    print("task saved to",filename)

def load_tasks(filename):
    global tasks
    try:
        with open(filename,"rb") as file:
            tasks = pickle.load(file)
        print("task loaded from",filename)
    except FileNotFoundError:
        print("file not found:",filename)

while True:
    print("\n---To-Do List App-----------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Task")
    print("4. Save Task")
    print("5. Load Task")
    print("6. Quit")


    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("enter task: ")
        remove_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        filename = input("enter filename to save tasks: ")
        save_tasks(filename)
    elif choice == "5":
        filename = input("enter filename to load tasks from: ")
        load_tasks(filename)
    elif choice =="6":
        print("goodbye!")

        break
    else:
        print("invalid choice. please choose a valid option.")