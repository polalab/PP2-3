class Person:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.citizenship = []



katrina = Person()
katrina.first_name = "Katrina"
katrina.last_name = "Rimsa"
katrina.age = 20
katrina.citizenship = ['Latvian']

print(katrina.first_name, katrina.last_name)


# we can also do:

class Person2:

    def __init__(self, first_name, last_name, age, citizenship):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.citizenship = citizenship

    def first_last_name(self):
        # method
        return self.first_name + self.last_name

    def calculate_age(self, year):
        # TODO: @katrinarimsa
        """Method calculates what year the person was born"""
        pass


katrina2 = Person2('Katrina', 'Rimsa', 20, ['Latvian'])
print(katrina.first_name, katrina.last_name)

print(katrina2.first_last_name())
print(katrina2.calculate_age(2023))
