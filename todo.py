def add(ite,ls):
    ls.append(ite)

def dele(y,li):
    li. remove(y)
    print("ITEMS IN TO DO LIST AFTER DELETION ARE:")
    for i in todo:
        print("\n",i)

def upd(z,lo,le):
    le.append(z)
    lo.remove(z)
todo = ["swim","read","fly"]
ach = ["iron","dance"]
while(1):
    n = int (input("\n enter the option\n 1. Add a task \n 2.View all task \n 3.Rmove a task \n4. Complete a task \n 5. Exit"))
    if(n ==1):
        it = input("Enter the name of task to be added:")
        add(it,todo)
        print("task added succesfully")
    if (n == 2):
        print("The items in to do list are")
        for i in todo:
            print(i,"\n")
    if (n == 3):
        n = input("Enter the name of task to be deleted:")
        if x in todo:
            dele(x, todo)
        else:
            print("the item not in the list")
    if (n == 4):
        l =  input("Enter task name doned")
        if l in todo:
            upd(l,todo,ach)
            print("\n TASK MARKED AS DONE")
            print("\nITEM IN ACHEIVED TASKS ARE:")
            for i in ach:
                print("\n", i)
            else:
                print("ITEMS IS NOT IN THE TODO LIST")
    if(n == 5):
        exit(0)
