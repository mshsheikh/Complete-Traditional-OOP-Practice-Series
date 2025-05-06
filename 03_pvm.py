class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1  # increment count
    
    @classmethod
    def show_count(cls):
        print(f"Total cars created: {cls.count}")

class Car(Counter):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand  # public variable
    
    def start(self):  # public method
        print(self.brand, "car goes vroom!")

num_cars = int(input("How many cars do you want to create? "))

for _ in range(num_cars):
    brand = input("Enter car brand: ")
    car = Car(brand)
    print("Brand:", car.brand)
    car.start()

Counter.show_count()