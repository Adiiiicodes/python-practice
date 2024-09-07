class library :
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def print_books(self):
        if(self.no_of_books==0):
            print('No Books In Library')
        else :
            print(f'The Number of books in library are {self.no_of_books} and these are the books :')
            for book in self.books :
                print(book)

    def add_book(self , book_name):
        self.books.append(book_name)
        self.no_of_books+=1
    def get_no_of_books(self):
        return self.no_of_books

lib = library()

lib.add_book("Atomic Habits")
lib.add_book("The Power of Subconscious mind")

lib.print_books()

print(f'Total Number of books are {lib.get_no_of_books()}')