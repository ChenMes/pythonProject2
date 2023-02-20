
class Loan:
    def __init__(self, customer_id: str, book_id: int, loan_date: str, return_date=None, loan_id=None):
        self._loan_id = loan_id
        self._customer_id = customer_id
        self._book_id = book_id
        self._loan_date = loan_date
        self._return_date = return_date

    def get_loan_id(self):
        return self._loan_id

    def get_customer_id(self):
        return self._customer_id

    def get_book_id(self):
        return self._book_id

    def set_loan_date(self, loan_date):
        self._loan_date = loan_date
        return True

    def get_loan_date(self):
        return self._loan_date

    def get_return_date(self):
        return self._return_date
