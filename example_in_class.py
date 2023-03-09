"""Imagine you have a bunch of students in your university class and you want to keep
track of all their grades, names and age in an easy way.
Now for each student you also want to assign a partner and also store that in a way.

Define a method that will return either name of the self or the partners name depending on whose grade is higher
"""

class Classmate:
    def __init__(self, first_name, last_name, grades, age):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
        self.age = age
        self.partner = None
    def whose_name(self):

        if self.grades > self.partner.grades:
            return self.first_name
        elif  self.grades < self.partner.grades:
            return self.partner.first_name
        else:
            return self.first_name + " and " + self.partner.first_name

    def __eq__(self, other):
        if not isinstance(other, Classmate):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


# return comparison





Laszlo = Classmate("Laszlo", "Spit", 4, 7)
Victoria = Classmate("Victoria", "Verhulst", 9, 20)
Pola = Classmate("Pola", "Lab", 7, 19)
Katrina = Classmate("Katrina", "Rimsa", 10, 21)

list_of_classmates = [Laszlo, Victoria, Pola, Katrina]

Laszlo.partner = Victoria  # type Classmate
Victoria.partner = Laszlo

def sort_class(list_of_classmates):
    sorted(list_of_classmates)
    return list_of_classmates

def print_class_list(list_of_classmates):
    lista = []
    for person in list_of_classmates:
        lista.append(person.first_name)
    return lista

list_of_classmates = [Laszlo, Victoria, Pola, Katrina]
print(print_class_list(list_of_classmates))

list_of_classmates = sorted(list_of_classmates)
#print(print_class_list(list_of_classmates))


#print(Victoria.partner.first_name)
