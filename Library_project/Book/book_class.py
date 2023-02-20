from datetime import datetime

from Library_project.library_validators import check_name, check_loan_type


class Book:
    def __init__(self, book_id: int, name: str, author: str, year_pub: int, loan_type: int):
        self._book_id = book_id
        self._name = name
        self._author = author
        self._year_pub = year_pub
        self._loan_type = loan_type

    def get_id(self):
        return self._book_id

    def set_newname(self, new_name: str):
        self._name = check_name(new_name)
        return True

    def get_name(self):
        return self._name

    def set_author(self, new_author):
        self._author = check_name(new_author)
        return True

    def get_author(self):
        return self._author

    def set_year_pub(self, year: str):
        if year.isdigit() and -5000 < int(year) <= datetime.now().year:
            self._year_pub = int(year)
        else:
            raise TypeError

    def get_year_pub(self):
        return self._year_pub

    def set_loan_type(self, loan_type: str):
        self._loan_type = check_loan_type(loan_type)

    def get_loan_type(self):
        return self._loan_type
