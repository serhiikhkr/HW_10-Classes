from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone.value not in [ph.value for ph in self.phones]:
            self.phones.append(new_phone)

    def delete_phone(self, phone):
        for ph in self.phones:
            if phone == ph.value:
                self.phones.remove(ph)

    def change_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if old_phone == ph.value:
                self.delete_phone(old_phone)
                self.add_phone(new_phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
