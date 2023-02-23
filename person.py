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

#print(katrina.first_name, katrina.age)


# we can also do:

class Person2:

    def __init__(self, first_name, last_name, age, citizenship, eye_color="red"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.citizenship = citizenship
        self.eye_color = eye_color

    def first_last_name(self):
        # method
        return self.first_name + self.last_name

    def calculate_age(self, year):
        """Method calculates what year the person was born"""
        return year - self.age


katrina2 = Person2('Katrina', 'Rimsa', 20, ['Latvian'], "blue")
#print(katrina2.first_name, katrina2.last_name, katrina2.eye_color)

katrina2.eye_color = "blue"
#print(katrina2.first_name, katrina2.last_name, katrina2.eye_color)

#print(katrina2.first_last_name())
print(katrina2.calculate_age(2023))
