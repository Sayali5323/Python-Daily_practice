try:
    with open("task.txt") as f:#when we use with func no need to close file,with func take cares
        tasks=f.readlines()#reads all lines into a list
        for i, task in enumerate (tasks,start=1):#enumerate give each item a number
            print(i,task.strip())#strips whitespaces

except FileNotFoundError:
    print("File not found")

