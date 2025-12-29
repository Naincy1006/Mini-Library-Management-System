print("              Welcome to Library     \n\n     ")
class Library:
    def __init__(self,book_list,library_name):
        self.book_list=book_list
        self.library_name=library_name
        self.book_lent={}
       
    def display_book(self):
       print("These are the books we have.",self.book_list)
    def lend_book(self):
        name=input("Please enter your name.")
        book=input("Please enter the name of book.")
        if book in self.book_list:
            self.book_list.remove(book)
            self.book_lent[name]=book
            print("The book has been lent successfully.")
            print(self.book_lent)
        elif book in self.book_lent.values():
         for person, borrowed_book in self.book_lent.items():
          if borrowed_book == book:
            print(f"This book is already taken by {person}")
        else:
           print("Invalid input.")
    def add_book(self):
           book=input("Please enter the name of book you want to add.")
           self.book_list.append(book)
    def book_returned(self):
           book = input("Enter the name of book you want to return: ")
           for person, borrowed_book in list(self.book_lent.items()):
                 if borrowed_book == book:
                  self.book_list.append(book)
                  del self.book_lent[person]
                 print("Book returned successfully.")
                 return
           
           print("Invalid input.This book was not lent from this library.")
if __name__=='__main__':
               
               book_list=["Atomic Habits","Rich Dad Poor Dad","The Alchemist"]
               ben_library=Library(book_list,"Ben's Library")
while True:
               user=input("Enter D to display books ,\n"
               "A to add the book in library ,\n"
               "L to lend the book from library ,\n"
               "R to return the book to library \n"
               "and E to exit the library. \n\n ").upper()
               if user=="E":
                   break 
               elif user=="D":
                   ben_library.display_book()
               elif user=="L":
                   ben_library.lend_book()
               elif user=="A":
                   ben_library.add_book()
               elif user=="R":
                   ben_library.book_returned()
                   
                   
               
           
           
