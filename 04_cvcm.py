class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(84, 86))
print(MathUtils.add("Hello ", "World"))

# (static methods)
mu = MathUtils()
print(mu.add(2, 4))