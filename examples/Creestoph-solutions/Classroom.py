class AlreadyInClassException(Exception):
    pass


class Classroom:
    def __init__(self, max):
        self.students = {}
        self.max_number = max

    def add_student(self, student):
        if len(self.students) > self.max_number or self.has_student(student.id):
            raise AlreadyInClassException
        self.students[student.id] = student

    def remove_student(self, student):
        if self.has_student(student.id):
            del self.students[student.id]

    def has_student(self, id):
        return id in self.students.keys()


class Student:
    def __init__(self, id, first_name, last_name, courses):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = list(courses)


a = Classroom(10)
s1 = Student(1,"Krzysiek", "Strzelecki", "Informatyka")
s2 = Student(2,"Adam", "Bobowski", ("Informatyka", "Costam"))
a.add_student(s1)
a.add_student(s2)
a.remove_student(s1)
a.remove_student(s1)
print(a.has_student(1))
