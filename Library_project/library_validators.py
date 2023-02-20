import re
from datetime import datetime, timedelta

from Library_project.Library_Exceptions import WrongFormat, NotInRange


def check_name(name: str):
    pattern = '^([A-Z][a-z]*) +([A-Z][a-z]*)$'
    if re.fullmatch(pattern, name):
        return name
    else:
        raise WrongFormat(f'"{name}" is not in format of typical name.')


def check_email(email: str):
    pattern = '[^@]+@[^@]+\.[^@]+'
    if re.fullmatch(pattern, email):
        return email
    else:
        raise WrongFormat(f'"{email}" is not in format of typical email.')


def check_customer_id(customer_id):
    pattern = '^[0-9]{9}$'
    if re.fullmatch(pattern, customer_id):
        return customer_id
    else:
        raise WrongFormat(f'"{customer_id}" is not in format of typical ID.')


def check_year(year: str):
    if year.isdigit():
        if -5000 <= int(year) <= datetime.now().year:
            return int(year)
        else:
            raise NotInRange(f'{year} should be between -5000 to {datetime.now().year}.')
    else:
        raise TypeError('Please enter ONLY digits')


def check_loan_type(loan_type: str):
    if loan_type.isdigit():
        if 1 <= int(loan_type) <= 3:
            return int(loan_type)
        else:
            raise NotInRange(f'{loan_type} should be between 1 to 3.')
    else:
        raise TypeError('Please enter ONLY digits')


def check_date(date: str):
    style = '%d/%m/%Y'
    if type(datetime.strptime(date, style)) == datetime:
        return datetime.strptime(date, style).strftime('%d/%m/%Y')
    else:
        raise WrongFormat(f'"{date}" is not in format of typical date.')


def get_id_from_file(type_id: str):
    current_id = None
    path = None
    match type_id:
        case 'book':
            path = "C:\\Users\\chenm\\PycharmProjects\\pythonProject1\\main\\Library_project\\Book\\book_id.txt"
        case 'loan':
            path = "C:\\Users\\chenm\\PycharmProjects\\pythonProject1\\main\\Library_project\\Loan\\loan_id.txt"
    with open(path, "r") as f:
        current_id = int(f.read())
    with open(path, "w") as f:
        f.write(str(current_id + 1))
    return current_id


# get_last_day_to_returned
def get_returned_date(loan_type: int, loan_date):
    days = 0
    if loan_type == 1:
        days = 10
    elif loan_type == 2:
        days = 5
    elif loan_type == 3:
        days = 2
    return_date = datetime.strptime(check_date(loan_date), '%d/%m/%Y') + timedelta(days=days)
    return return_date


# validate_return_loan
def check_return_loan(loan_type, loan_date, return_date):
    if get_returned_date(loan_type, check_date(loan_date)) >= datetime.strptime(check_date(return_date), '%d/%m/%Y'):
        return True
    else:
        return False
