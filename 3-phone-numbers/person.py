class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        return self.normalize_phone_number(self._phone_number) == self.normalize_phone_number(input_phone_number)

    def get_name(self):
        return self._name

    @staticmethod
    def normalize_phone_number(phone_number):
        norm_number = ""
        for n in str(phone_number):
            if n.isdigit() or n in ("x", "/"):
                norm_number += n
        return norm_number