from pprint import pprint

from Library_project.Customer.customer_class import Customer
from Library_project.Library_Exceptions import CustomerAlreadyExist, CustomerNotFound
from Library_project.Main_run import library
from Library_project.file_hendler import fetch_all, add_object_to_file, write_all
from Library_project.library_validators import check_customer_id, check_name, check_email, check_date


def add_new_customer():
    # Collecting details from user and creating a customer.
    customer_id = check_customer_id(input('ID(Must be 9 numbers):'))
    name = check_name(input('Name(First and last, With a Capitol letters):'))
    address = input('Address:')
    email = check_email(input('eMail:'))
    birthd = check_date(input('Birthdate:(dd/mm/yyyy)'))
    customer = Customer(customer_id, name, address, email, birthd)

    # Checking if customer is already exist.
    customers_list = fetch_all('customers')
    for cust in customers_list:
        if cust['id'] == customer_id:
            raise CustomerAlreadyExist(f'A customer with ID: {customer_id} is already exist in the library.')
        else:
            add_object_to_file(customer, 'customer')
            print(f'{name} is now a customer!')
    return True


def display_all_customers():
    pprint(fetch_all('customers'))


def remove_customer_from_the_library():
    # Validating details from user.
    customer_id = input('Customer ID: ')
    customers = library.get_customers()

    # Searching for customer details and removing from library.
    for customer in customers:
        if customer['id'] == customer_id:
            customers.remove(customer)
            write_all('customers', customers)
            print('Delete customer successfully')
    raise CustomerNotFound(f'ID: {customer_id} is not a customer in the library.')


def find_customer_by_name():
    # Validating details from user.
    customer_name = check_name(input("Customer's name: "))
    customers = fetch_all('customers')

    # Searching customer by name.
    for customer in customers:
        if customer['name'] == customer_name:
            print(customer)
            return customer
    raise CustomerNotFound(f'{customer_name} is not a customer in the library.')
