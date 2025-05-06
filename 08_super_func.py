class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

if __name__ == "__main__":
    t = Teacher("Mr. Salman", "Python")
    print(f"Name: {t.name}, Subject: {t.subject}")