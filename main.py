import os

def addTask(taskName, taskDescription):
    with open("tasks.txt", "a") as f:
        f.write(f"{taskName}:{taskDescription}\n")
    print("\n[+] New Task Added!\n")

while True:
    operation = input("-----To-Do-----\n1-Tasks\n2-Add Task\n3-Remove Task\n99-Save & Quit\n\n>>")

    if operation == "1":
        os.system("cls")
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                print("-----Tasks-----\n")
                for x  in f:
                    taskName = x.split(":", 1)[0]
                    taskDesc = x.split(":", 1)[1]

                    print(f"Task Name : {taskName} | Task Description : {taskDesc}\n")
                print("---------------")
        else:
            f = open("tasks.txt", "w")
            f.write("")
            f.close()

    if operation == "2":
        name = input("\nEnter the tasks name : ")
        desc = input("Enter the description of task : ")
        addTask(name, desc)

    if operation == "3":
        nameOfTask = input("\nEnter the name of the task : ")
        with open("tasks.txt", "r") as f:
            lines = f.readlines()

        with open("tasks.txt", "w") as f:
            removed = False
            for line in lines:
                if not line.startswith(nameOfTask):
                    f.write(line)
                else:
                    removed = True
    
    if operation == "99":
        exit()