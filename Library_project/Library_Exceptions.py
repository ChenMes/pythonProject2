class LibraryExceptions(Exception):
    def __int__(self, msg):
        super().__init__(msg)


class UnMatchedID(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)


class WrongFormat(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)


class BookNotFound(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)


class BookNotAvailable(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)


class CustomerNotFound(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)


class NotInRange(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)


class CustomerAlreadyExist(LibraryExceptions):
    def __int__(self, msg):
        super().__init__(msg)
