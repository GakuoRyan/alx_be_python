class Book:
    def __init__(self,title, author):
        self.title = title
        self.author =author
        self._is_checked_out = False
    def check_out(self):
        print("Mark the book as checked out.")
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        print("Mark the book as returned.")
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    def is_available(self):
        print("Check if the book is available.")
        return not self._is_checked_out
