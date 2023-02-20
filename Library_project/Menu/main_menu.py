from Library_project.Menu.books import add_new_book, display_all_books, find_books_by_name, find_books_by_author, \
    remove_book_from_the_library
from Library_project.Menu.customers import add_new_customer, display_all_customers, find_customer_by_name, \
    remove_customer_from_the_library
from Library_project.Menu.loans import loan_a_book, return_a_book, display_all_loans, display_all_the_late_loans, \
    display_past_loans_for_specific_customer, display_current_loans_for_specific_customer

main_menu = """
------ Main menu: ------

what do you want to do?
1 - add new customer
2 - add new book
3 - loan book
4 - return a book
5 - display all books
6 - display all customers
7 - display all loans
8 - display all late loans
9 - display loans for a specific customer 
10 - find book by name
11 - find book by author
12 - find customer by name 
13 - remove all books from the library 
14 - remove all customers from the library

"""

cases = range(1, 15)


def menu():
    while True:
        try:
            print(main_menu)
            choice = int(input("enter your choice: "))
            if choice in cases:
                match choice:
                    case 1:
                        add_new_customer()
                    case 2:
                        add_new_book()
                    case 3:
                        loan_a_book()
                    case 4:
                        return_a_book()
                    case 5:
                        display_all_books()
                    case 6:
                        display_all_customers()
                    case 7:
                        display_all_loans()
                    case 8:
                        display_all_the_late_loans()
                    case 9:
                        display_past_loans_for_specific_customer()
                    case 10:
                        display_current_loans_for_specific_customer()
                    case 11:
                        find_books_by_name()
                    case 12:
                        find_books_by_author()
                    case 13:
                        find_customer_by_name()
                    case 14:
                        remove_book_from_the_library()
                    case 15:
                        remove_customer_from_the_library()
                    case 16:
                        exit()

        except Exception as e:
            print(e)
            pass
