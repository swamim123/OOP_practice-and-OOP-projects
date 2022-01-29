class library:


    def __init__(self, Name, List):
        self.name= Name
        self.list= List
        self.dict={}

    @staticmethod
    def continuee():
        print("What operation you want to perform?")
        print("1.Display Book")
        print("2.Lend Book")
        print("3.Add Book")
        print("4.Return Book")

    def display(self):
        return f"The available books are:\n{self.list}"

    def lend(self):
        book_name=input("Enter the book that you want to lend:\n")
        user_name=input("Enter your name:\n")

        if book_name in self.list:
            if book_name not in self.dict.keys():
                self.dict.update({book_name: user_name})
                return f"Done!you can now lend{book_name}"
            else:
                return f"The book is already owned by{self.dict[book_name]}"
        else:
            return f"Sorry the book you have enterd is not available in our library"

    def add(self):
        name_book= input("Enter the name of the book that you want to add:\n")
        self.list.append(name_book)
        return f"{name_book} book has been added successfuly"

    def returnb(self):
        returnbook=input("Enter which book you want to return:\n")
        returnname=input("Ener your name:\n")

        if returnbook in self.dict.keys() and returnname in self.dict.values():
            self.dict.pop(returnbook)
            return F"Successfuly returned the book."
        else:
            return f"Sorry {returnname} you have not lent {returnbook}"

Virat= library("Virat", ["Story","poem","Novel","songs","Coding book"])
while True:
    Virat.continuee()
    user_input= input()
    if user_input== "1":
        print(Virat.display())
    elif user_input=="2":
        print(Virat.lend())
    elif user_input=="3":
        print(Virat.add())
    elif user_input=="4":
        print(Virat.returnb())
    else:
        print("Please enter 1/2/3/4 only")

    Ask=("Do you want to continue? Enter Y for yes N for NO:\n")
    if Ask== "Y" :
        continue
    elif Ask == "N" :
        exit()
    else:
        print("Enter Y or N only.")


