#Empty list to store tasks

todo_list=[]

while True:
    print("\n----TO-DO LIST----")
    print("1. Show Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice=input("Enter your choice(1-4): ")

    if choice =="1":
        if len(todo_list)==0:
            print("\n No Tasks yet!")
        else:
            print("\n Your tasks: ")
            for i, task in enumerate(todo_list,1):
                print(f"{i},{task}")

    elif choice=="2":
        task= input("Enter the task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice==3:
        if len(todo_list)==0:
            print("No tasks to remove.")
        else:
            print("Which task number to remove? ")
            for i, task in enumerate(todo_list,1):
                print(f"{i}.{task}")
            try:
                task_num=int(input("Enter task number:"))

                if 1<=task_num<=len(todo_list):
                    removed=todo_list.pop(task_num-1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number.")

    elif choice==4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.Please Choosw from 1 to 4")
