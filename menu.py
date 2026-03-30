l=list(map(int,input("Enter elements of list separated by using space: ").split()))
while(1):
    print("\t\tMENU")
    print("1.Maximum value")
    print("2.Minimum value")
    print("3.Slicing of list")
    print("4.Occurence of an item")
    print("5.First occourence of an item")
    print("6.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Maximum value of the list:",max(l))
    elif choice==2:
        print("Minimum value of the list:",min(l))
    elif choice==3:
        print("Slicing the List")
        s=int(input("Enter starting index: "))
        e=int(input("Enter ending index: "))
        print("Sliced List:",l[s:e])
    elif choice==4:
        item=int(input("Enter an item/element: "))
        print("Occurence:",l.count(item))
    elif choice==5:
        item=int(input("Enter an item/element: "))
        if item in l:
            print("First Occurence found at index:",l.index(item))
        else:
            print("Item not found..")
    elif choice==6:
        print("Exit")
        break
    else:
        print("Invalid Choice")
