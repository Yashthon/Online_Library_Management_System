print("\tWELCOME TO \b MY LIBRARY.\b")
print("*****************************")


class Library:

    def __init__(self, List_of_books, Library_name):
        self.List_of_books = List_of_books
        self.Library_name = Library_name
        self.ami = ami = {'The COSMOS': 'Yash'}
        self.List_of_books = ['*The COSMOS', '*Spacetime and Geometry - An Introduction to General Relativity ',
                              '*A Brief History of Time', '*The fabric of Cosmos', '*Space-Time']

    def Donate_a_Book(self, Donate):
        self.Donate = self.List_of_books.append(Donate)
        for item in self.List_of_books:
            print(item)

    def display(self):
        for item in self.List_of_books:
            print(item)

    def Lend_a_Book(self, Book_Name, Lender_Name):

        if Book_Name in self.List_of_books:
            if Book_Name in self.ami:
                for key, value in self.ami.items():
                    if Book_Name in key:
                        print(f"Sorry This book is lent by {value}")
            if Book_Name not in self.ami:
                self.ami[Book_Name] = Lender_Name

                print("success")
                print(self.ami)

        else:
            print("Sorry, this book is not available right now.")

    def Return_Book(self, ret):
        del self.ami[ret]
        print("Book returned successfully!")
        print(self.ami)


My_Library = Library("List_of_books", "My_Library")

while True:
    print("\nEnter 0 to exit the library ")
    print("Enter 1 to Donate new book ")
    print("Enter 2 to display books ")
    print("Enter 3 to lend the book ")
    print("Enter 4 to return the lent book\n ")
    i = input()

    if i == '1':
        print("Enter the name of the book -->")
        i2 = input()
        My_Library.Donate_a_Book(i2)

    if i == '2':
        My_Library.display()

    if i == '3':
        i3 = input("Which book do you want?\n")
        i4 = input("What is your name?\n")
        My_Library.Lend_a_Book(i3, i4)

    if i == '4':
        i5 = input("What is your name?\n")
        i6 = input("Which book do you want to return?\n")
        My_Library.Return_Book(i6)

    if i == '0':
        quit()
