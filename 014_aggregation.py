class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

class Employee:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    emp = Employee("John Doe")
    dept = Department("HR", emp)
    print(f"Department Manager: {dept.manager.name}")