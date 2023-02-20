from Library_project import file_hendler
from Library_project.Library_Exceptions import UnMatchedID
from Library_project.library_validators import check_customer_id


class Library:
    def __init__(self):
        self._customers = []
        self._books = []
        self._loans = []

    def get_customers(self):
        self._customers = file_hendler.fetch_all('customers')
        return self._customers

    def get_books(self):
        self._books = file_hendler.fetch_all('books')
        return self._books

    def get_loans(self):
        self._loans = file_hendler.fetch_all('loans')
        return self._loans

    def get_book_by_id(self, book_id: str):
        books = self.get_books()
        if type(book_id) == int:
            for book in books:
                if int(book["book_id"]) == int(book_id):
                    return book
            raise UnMatchedID(f'Book ID:{book_id} is not found in the library')
        raise TypeError('Please enter ONLY digits')

    def get_customer_by_id(self, customer_id):
        customers = self.get_customers()
        checked_id = check_customer_id(customer_id)
        for customer in customers:
            if customer['id'] == checked_id:
                return customer


library = Library()
