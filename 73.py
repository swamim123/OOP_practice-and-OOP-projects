no_items= int(input("Enter how many items you want to print:"))
no_names= input("Enter the name of items:")
list= no_names.split()
t = int(input(("Which type of compherihence you want to chosse.\n1 1.List 2.Dict 3.set:")))

if t==1:
    ls= [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1= {f"item{i}": i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    set1= {i for i in list}
    print(set1)
    print(type(set1))
