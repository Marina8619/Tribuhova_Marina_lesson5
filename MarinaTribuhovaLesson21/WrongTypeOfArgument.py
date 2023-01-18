class CustomExceptionBase(Exception):
    def __init__(self):
        self.message = "Common exception"

    def __str__(self):
        return f"The function raised an exception {self.message}"


class WrongTypeOfArgument(CustomExceptionBase):
    def __init__(self):
        self.message = "Wrong argument type"



