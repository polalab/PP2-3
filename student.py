"""Homework"""
#1.
class Student:
    def __init__(self, name, age, nationalities, course_grades ):
        self.name = name
        self.age = age
        self.nationalities = nationalities
        self.course_grades = course_grades

#2.
    def checking(self):
        return self.course_grades  #just to check

    def what_classes(self):
        return list(self.course_grades.keys())

    def mean_grades(self):
        res = sum(self.course_grades.values()) / len(self.course_grades)
        return str(res)


#3.
course_grades = {}
Victoria = Student('Verhulst', 20, ('dutch'), {'math': 9, 'english': 10})
Pola = Student('Labedzka', 20, ('polish', 'american'), {'math': 10, 'english': 10})
Katrina = Student('Rimsa', 21, ('latvian', 'italian'), {'math': 8, 'english': 10})

print(Victoria.what_classes())
my_students = [Victoria, Pola, Katrina]
#my_students = []
#my_students.append(Student('Victoria'))
#my_students.append(Student('Pola'))
#my_students.append(Student('Katrina'))

#4.
def highest_mean(my_students):
    known_highest = -1
    known_name = ""
    for person in my_students:
        if known_highest < float(person.mean_grades()):
            known_highest = float(person.mean_grades())
            known_name = person.name
    return known_name

print(highest_mean(my_students))





