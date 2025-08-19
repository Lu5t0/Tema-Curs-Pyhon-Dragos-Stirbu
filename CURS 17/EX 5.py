class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)

    def calcul_medie(self):
        if not self.grades:
            return None
        return sum(self.grades)/len(self.grades)
    def __str__(self):
        return f"Student:{self.name}, Age: {self.age}, Grades: {self.grades}"

if __name__ == '__main__':
    student = Student("Mihai", 23 )
    student.add_grade(9)
    student.add_grade(6)
    print(student)

    medie = student.calcul_medie()
    if medie is not None:
        print(f"Media notelor este {medie:.2f}")
    else:
        print("Nu există note pentru a calcula media.")


