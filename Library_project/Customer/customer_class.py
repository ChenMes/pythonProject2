from Library_project.library_validators import check_name, check_email


class Customer:
    def __init__(self, customer_id: str, name: str, address: str, email: str, birthd: str, suspend_time=None):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email
        self.birthd = birthd
        self._suspended_time = suspend_time

    def get_customer_id(self):
        return self.customer_id

    def set_name(self, name):
        self.name = check_name(name)

    def get_name(self):
        return self.name

    def set_address(self, address: str):
        if type(address) is str:
            self.address = address
        else:
            raise TypeError

    def get_address(self):
        return self.address

    def set_email(self, email):
        self.email = check_email(email)

    def get_email(self):
        return self.email

    def get_birthd(self):
        return self.birthd

    def get_suspended_time(self):
        return self._suspended_time

    def set_suspended_time(self, date):
        self._suspended_time = date
