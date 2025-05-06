class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private

if __name__ == "__main__":
    emp = Employee("Salman", 6000000, "123-45-6789")

    print("Accessing public variable name:", emp.name)
    print("Accessing protected variable _salary:", emp._salary)
    
    try:
        print("Accessing private variable __ssn:", emp.__ssn)
    except AttributeError as e:
        print("Error accessing __ssn:", e)

    print("Accessing private variable via name mangling:")