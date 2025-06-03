class Book:
    def __init__(self, author,title,ISBN):
        self.author = author
        self.title = title
        self.ISBN = ISBN
    def get_details(self):
        print(f"Author: {self.author} \ Book Title: {self.title} \ ISBN: {self.ISBN}")
    
class FictionBook(Book):
    def __init__(self,author,title,ISBN,genre):
        super().__init__(author,title,ISBN)
        self.genre = genre
    def get_details(self):
        return f"{super().get_details()} \ Genre: {self.genre}"

class NonFictionBook(Book):
    def __init__(self,author,title,ISBN,genre):
        super().__init__(author,title,ISBN)
        self.genre = genre
    def get_details(self):
        return f"{super().get_details()} \ Genre: {self.genre}"
    


        