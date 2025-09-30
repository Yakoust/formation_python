class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email

    def show(self):
        print(self.name + ' - ' + self.email)


class Contact(Address, Person):

    def __init__(self, street, city, name, email):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)

    def show(self):
        print(self.name + " - " + self.email)
        print(self.street)
        print(self.city)

class Notebook:
    def __init__(self):
        self.contacts = []

    def add(self, name, email, street, city):
        self.contacts.append(Contact(street, city, name, email))

    def show(self):
        for contact in self.contacts:
            print(f"=== {contact.name} ===")
            contact.show()

notes = Notebook()
notes.add('Alice', '<alice@example.com>', 'Lv 24', 'Sthlm')
notes.show()