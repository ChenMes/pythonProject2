from pprint import pprint

from Library_project.Book.book_class import Book
from Library_project.Library_Exceptions import BookNotFound, BookNotAvailable
from Library_project.Main_run import library
from Library_project.Menu.loans import is_book_available
from Library_project.file_hendler import add_object_to_file, fetch_all, write_all
from Library_project.library_validators import get_id_from_file, check_name, check_loan_type, check_year


def add_new_book():
    # Get information from user
    book_id = get_id_from_file('book')
    name = input("Book's name: ")
    author = check_name(input("Author's name: "))
    year_published = check_year(input('Year of published: '))
    loan_type = check_loan_type(input('loan type(1/2/3): '))

    # Creating a new book and adding to json file.
    book = Book(book_id, name, author, year_published, loan_type)
    add_object_to_file(book, 'book')
    return True, print(f'{name}, Written by: {author} has been added to the library!')


def display_all_books():
    pprint(fetch_all('books'))


def find_books_by_name():
    # Get information from user
    book_name = input("Book's name: ")
    books = fetch_all('books')

    # Searching book by name.
    for book in books:
        if book['book_name'] == book_name:
            pprint(book)
    raise BookNotFound(f'Cant find {book_name} in the library.')


def find_books_by_author():
    # Get information from user
    author_name = check_name(input("Author's name: "))
    books = fetch_all('books')

    # Searching book by author name.
    for book in books:
        if book['author_name'] == author_name:
            pprint(book)
    raise BookNotFound(f'{author_name} has no books in the library')


def remove_book_from_the_library():
    # Get information from user
    book_id = input('Book ID: ')
    books = library.get_books()

    # If removing conditions are possible, removing book from json file.
    if is_book_available(book_id):
        for book in books:
            if int(book['book_id']) == book_id:
                books.remove(book)
                write_all('books', books)
                print('Delete book successfully')
                return True
            raise BookNotFound(f'Book ID:{book_id} is not found in the library')
    else:
        raise BookNotAvailable(f'Book number {book_id} is already loaned.')
