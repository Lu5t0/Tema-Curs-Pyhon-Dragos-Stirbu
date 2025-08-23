class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

class Student(Person):
    def __init__(self, grades, **kwargs):
        self.grades = grades
        super().__init__(**kwargs)

class Teacher(Person):
    def __init__(self, subject, **kwargs):
        self.subject = subject
        super().__init__(**kwargs)

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, grades, subject):
        super().__init__(name=name, age=age, grades=grades, subject=subject)

    def __str__(self):
        return f"{self.name}, {self.age} ani, predă {self.subject}, note: {self.grades}"

# Executare doar dacă fișierul e rulat direct
if __name__ == "__main__":
    ta = TeachingAssistant("Andrei Popescu", 24, [9, 10, 8], "Matematică")
    print(ta)