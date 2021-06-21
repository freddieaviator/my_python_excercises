class Person(object):
    
    def __init__(self,first_name,last_name,birthyear,domain = None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthyear = birthyear
        self.domain = domain


    def __repr__(self):
        return f"""Person({self.first_name},{self.last_name},{self.birthyear},{self.city},{self.zip_code},{self.email})"""
        
    @property
    def email(self):
        if self.domain == None:
            return f"{self.first_name}.{self.last_name}@{self.default_domain}"
        else:
            return f"{self.first_name}.{self.last_name}@{self.domain}"

    def age(self):
        return 2021 - int(self.birthyear)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self,name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last
    
    default_domain = "online.com"

class Employee(Person):
    def __init__(self, first_name, last_name, birthyear, salary):
        super().__init__(first_name, last_name, birthyear)
        self.salary = salary
        self.customers = []

    def add_customer(self,customer):
        self.customers.append(customer)
    
    def drop_customers(self):
        self.customers = []

    def print_earnings(self):
        print()

        
    
    default_domain = "academy.com"


fredrik = Employee("Fredrik","Hårberg","1988","20000")
print(fredrik.__dict__)
fredrik.add_customer("Henrik Hårberg")
print(fredrik.__dict__)
fredrik.drop_customers()
print(fredrik.__dict__)