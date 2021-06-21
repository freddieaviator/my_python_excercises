class Person(object):
    
    def __init__(self,first_name,last_name,birthyear,domain = None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthyear = birthyear
        self.domain = domain


    def __repr__(self):
        return f"""Person({self.first_name},{self.last_name},{self.birthyear},{self.email})"""
        
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

class Customer(Person):
    def __init__(self, first_name, last_name, birthyear, domain,full_price):
        super().__init__(first_name, last_name, birthyear, domain)
        self.payed_price=0
        self.full_price = full_price
   
    def discount(self)->None:
        """ Sets the discounted price as payed_price 

        Arguments: None

        Returns: Nothing
        
        """
        self.payed_price = self.full_price - Person.age(self)

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
        earnings = 0
        for customer in self.customers:
            earnings += customer.payed_price 
        
        print(f"{self.full_name}, {Person.age(self)}, Earnings:{earnings}, Net-profit:{earnings - int(self.salary)}")

        
    
    default_domain = "academy.com"


fredrik = Employee("Fredrik","Hårberg","1988","20000")
henrik = Employee("Henrik","Hårberg","1992","100")
fredrik_c = Customer("Fredrik","Hårberg","1988","harberg.se",545)
julia_c = Customer("Julia","Hümpfner","1992","hümpfner.de",545)
henrik_c = Customer("Henrik","Hårberg","1992","harberg.se", 320)
fredrik_c.discount()
julia_c.discount()
henrik_c.discount()
fredrik.add_customer(fredrik_c)
fredrik.add_customer(julia_c)
henrik.add_customer(henrik_c)


print(fredrik.__dict__)
print(fredrik_c.payed_price)
print(julia_c.payed_price)

fredrik.print_earnings()

print(henrik.__dict__)
print(henrik_c.payed_price)
henrik.print_earnings()




