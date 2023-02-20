from datetime import datetime
from pprint import pprint

from Library_project.Book.book_class import Book
from Library_project.Library_Exceptions import BookNotAvailable
from Library_project.Loan.loan_class import Loan
from Library_project.Main_run import library
from Library_project.file_hendler import add_object_to_file, write_all, fetch_all
from Library_project.library_validators import check_customer_id, get_id_from_file, get_returned_date, check_return_loan


def is_book_available(book_id):
    for loan in library.get_loans():
        if book_id == int(loan['book_id']) and loan['return_date'] is not None:
            return False
    return True


def loan_a_book():
    # Validating details from user.
    customer_id = check_customer_id(input('Customer ID: '))
    book_id = input('Book ID: ')
    if book_id.isdigit():
        book_id = int(book_id)
    else:
        raise TypeError('Please enter ONLY digits')

    # Validating book availability and creating loan class loan.
    if is_book_available(book_id):
        book = library.get_book_by_id(book_id)
        loan_type = book["book_loan_type"]
        loan_id = get_id_from_file("loan")
        loan_date = datetime.date.today().strftime('%d/%m/%Y')
        loan = Loan(customer_id, book_id, loan_date,
                    str(get_returned_date(loan_type, loan_date)).split(' ')[0].replace("-", "/"), loan_id)
        add_object_to_file(loan, 'loan')
        customer = library.get_customer_by_id(customer_id)
        print(f'{book["book_name"]} has been loaned to {customer["name"]}')

        # Calculating return date.
        book = Book(book["book_id"], book["book_name"], book['author_name'], book['book_year_published'],
                    book['book_loan_type'])
        date = get_returned_date(book.get_loan_type(), loan_date)
        return_date = date.strftime('%d/%m/%Y')
        print(f'the return date is: {return_date}')
    else:
        raise BookNotAvailable(f'Book number {book_id} is already loaned.')


def return_a_book():
    # Validate details from user.
    customer_id = check_customer_id(input('Customer ID: '))
    customer = library.get_customer_by_id(customer_id)
    book_id = input('Book ID: ')
    if book_id.isdigit():
        book_id = int(book_id)

    # Validating availability
    if is_book_available(int(book_id)) is False:
        loans = library.get_loans()
        found_book = False
        for loan in loans:
            if loan["book_id"] == int(book_id):
                book = library.get_book_by_id(book_id)
                loan_type = book["book_loan_type"]
                return_date = datetime.date.today().strftime('%d/%m/%Y')

                # In case of return on time.
                if check_return_loan(loan_type, loan['loan_date'], return_date) is True:
                    loan["return_date"] = return_date
                    write_all('loans', loans)
                    print("Book returned")
                    return True

                # In case of return after return date.
                else:
                    suspended = datetime.date.today() + datetime.timedelta(days=14)
                    date_str = suspended.strftime('%d/%m%Y')
                    customer['suspended time'] = date_str
                    loan['return_date'] = return_date
                    write_all('loans', loans)
                    print('Book has returned to the library')
                    return True

        if not found_book:
            print("The book is not loaned")
    else:
        print("The book cannot be return because is in the library")


def display_all_loans():
    pprint(fetch_all('loans'))


def display_past_loans_for_specific_customer():
    customer_loans = []
    customer_id = check_customer_id(input('Enter customer ID: '))
    loans = library.get_loans()
    for loan in loans:
        if loan['customer_id'] == customer_id and loan['return_date'] is not None:
            customer_loans.append(loan)
    pprint(customer_loans)


def display_current_loans_for_specific_customer():
    customer_loans = []
    customer_id = check_customer_id(input('Enter customer ID: '))
    loans = library.get_loans()
    for loan in loans:
        if loan['customer_id'] == customer_id and loan['return_date'] is None:
            customer_loans.append(loan)
    pprint(customer_loans)


def display_all_the_late_loans():
    print("All the late loan: ")
    today = datetime.date.today()
    return_date = today.strftime('%d/%m/%Y')
    loans = library.get_loans()
    for loan in loans:
        if loan['return_date'] is None:
            book = library.get_book_by_id('book_id')
            loan_type = book["book_type_loan"]
            if check_return_loan(loan_type, loan['loan_date'], return_date) is False:
                print(loan)
