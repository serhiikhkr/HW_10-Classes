from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, t_phone):
        self.t_phone = t_phone


class Record:
    def __init__(self, name: str, phones_list=None):
        self.name = Name(name)
        self.phones = [Phone(phone).t_phone for phone in phones_list]

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def change_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = [record.phones]

