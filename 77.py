def new():
    import time
    book= " virat rohit dhwan ishant rahul bumrah jadeja mayank hardik kunal shami shardul dhoni"
    time.sleep(4)


    while True:
        text=(yield)
        if text in book:
            print("Text present in book")
        else:
            print("Text not present in book")

find=new()
print("findind now...")
next(find)
print("Again finding")
find.send("kohli")
find.send("virat")

