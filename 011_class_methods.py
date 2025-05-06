class Book:
    total_books = 0

    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

if __name__ == "__main__":
    b1 = Book()
    b2 = Book()
    print("Total books:", Book.total_books)