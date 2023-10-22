from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)  # Initialize Name field with a value

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a 10-digit number")
        super().__init__(value)  # Initialize Phone field with a validated value

class Record:
    def __init__(self, name):
        self.name = Name(name)  # Initialize Record with a Name field
        self.phones = []  # Initialize a list to store Phone objects

    def add_phone(self, phone):
        self.phones.append(Phone(phone))  # Add a Phone object to the list of phones

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)  # Remove a Phone object from the list

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone  # Edit a Phone object in the list

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value  # Find a Phone object in the list

    def __str__(self):
        phone_list = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_list}"  # Generate a string representation of the Record

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # Add a Record to the AddressBook

    def find(self, name):
        return self.data.get(name, None)  # Find a Record in the AddressBook by name

    def delete(self, name):
        if name in self.data:
            del self.data[name]  # Delete a Record from the AddressBook

if __name__ == "__main__":
    # Creating a new address book
    book = AddressBook()

    # Creating a new contact
    new_contact = Record("John")

    # Adding phone numbers to contacts
    new_contact.add_phone("1234567890")
    new_contact.add_phone("5555555555")

    # Adding a contact to address book
    book.add_record(new_contact)

    # Creating and adding a new record
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Printing all records of the book
    for name, record in book.data.items():
        print(record)

    # Finding and editing a phone number for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Printing: Contact name: John, phones: 1112223333; 5555555555

    # John Finding an exact phone number in a record John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")  # Printing: 5555555555

    # Deleting contact Jane
    book.delete("Jane")
