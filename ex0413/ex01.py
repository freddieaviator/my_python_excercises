class Person(object):
    
    def __init__(self,first_name,last_name,birthyear,city,zip_code,domain = None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthyear = birthyear
        self.city = city
        self.zip_code = zip_code
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

    def city_zip(self):
        return f"{self.city}, {self.zip_code}"
    
    default_domain = "online.com"
