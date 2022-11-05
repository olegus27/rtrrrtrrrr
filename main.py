class Human:
    def __init__(self,name = 'Human'):
        self.name = name

class Car:
    def __init__(self,brand):
        self.brand = brand
        self.passangers = []

    def add_passangers(self, human):
        self.passangers.append(human)

    def print_passangers_names(self):
        if self.passangers != []:
            print(f'Names of {self.brand} passengers')
            for passenger in self.passangers:
                print(passenger.name)
        else:
            print(f'There are no passenger in {self.brand}')

class Company:
    def __init__(self, brand):
        self.brand = brand
        self.employee = []

    def add_employee(self, human):
        self.employee.append(human)

    def print_employee_name(self):
        if self.employee != []:
            print(f'Name of {self.brand} employee')
            for employee in self.employee:
                print(employee.name)

        

nick = Human('Nick')
kate = Human('Kate')
edison = Human('Edison')
car = Car('Mercedes')
company = Company('Mercedes')

car.add_passangers(nick)
car.add_passangers(kate)
company.add_employee(edison)
car.print_passangers_names()
company.print_employee_name()
