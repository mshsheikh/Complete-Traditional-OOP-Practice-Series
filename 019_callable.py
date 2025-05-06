class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

if __name__ == "__main__":
    multiply_by_3 = Multiplier(3)
    print("callable(multiply_by_3):", callable(multiply_by_3))
    print("multiply_by_3(5):", multiply_by_3(5))