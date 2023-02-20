import json

from Library_project.Book.book_class import Book
from Library_project.Customer.customer_class import Customer
from Library_project.Loan.loan_class import Loan


# customers
def customer_to_customer_dict(customer) -> dict:
    return {
        "id": customer.get_customer_id(),
        "name": customer.get_name(),
        "address": customer.get_address(),
        "email": customer.get_email(),
        "birthdate": customer.get_birthd(),
        "suspended time": customer.get_suspended_time()
    }


# books
def book_to_book_dict(book) -> dict:
    return {
        "book_id": book.get_id(),
        "book_name": book.get_name(),
        "author_name": book.get_author(),
        "book_year_published": book.get_year_pub(),
        "book_loan_type": book.get_loan_type()
    }


# loans
def loan_to_loan_dict(loan) -> dict:
    return {
        "loan_id": loan.get_loan_id(),
        "customer_id": loan.get_customer_id(),
        "book_id": loan.get_book_id(),
        "loan_date": loan.get_loan_date(),
        "return_date": loan.get_return_date()
    }


def add_object_to_file(obj: Customer | Book | Loan, obj_type: str):
    file_path = ''
    object_dict = {}
    file_dict = []
    match obj_type:
        case 'customer':
            object_dict = customer_to_customer_dict(obj)
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Customer/customers.json'
        case 'book':
            object_dict = book_to_book_dict(obj)
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Book/books.json'
        case 'loan':
            object_dict = loan_to_loan_dict(obj)
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Loan/loans.json'
    with open(file_path, 'r') as f:
        file_dict = json.load(f)
    file_dict.append(object_dict)
    with open(file_path, 'w') as f:
        json.dump(file_dict, f)


def fetch_all(display_type):
    file_path = ''
    match display_type:
        case 'customers':
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Customer/customers.json'
        case 'books':
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Book/books.json'
        case 'loans':
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Loan/loans.json'
    with open(file_path, 'r') as f:
        content = json.load(f)
        return content


def write_all(write_type, object_to_write):
    file_path = ''
    match write_type:
        case 'customers':
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Customer/customers.json'
        case 'books':
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Book/books.json'
        case 'loans':
            file_path = 'C:/Users/chenm/PycharmProjects/pythonProject1/main/Library_project/Loan/loans.json'

    with open(file_path, 'w') as f:
        json.dump(object_to_write, f)
