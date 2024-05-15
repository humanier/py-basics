l = [2, 3, 5, 8]
x = list(['a', 'v', 'r'])

# print(l)
# l.append(34)
# print(l)
# l.pop()
# print(l)
# len(l)


# -------------------
class School:
    def __init__(self, students):
        self.__students = [x for x in students]

    def add_student(self, student_name):
        if len(self.__students) < 3:
            self.__students.append(student_name)

    def get_students(self):
        return self.__students
    
    def __str__(self):
        return 'School with ' + str(len(self.__students)) + ' students.'

    
school_13 = School(['Oleg', 'Maxim', 'Anna'])
school_7 = School(['Gena'])

# print('School #13:' + str(school_13.get_students()))
# school_13.add_student('Denis')
# print('School #13:' + str(school_13.get_students()))

print(school_13)
print(school_7)


# print('School #7:' + str(school_7.get_students()))
# school_7.add_student('Denis')
# print('School #7:' + str(school_7.get_students()))

