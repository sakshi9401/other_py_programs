class Calculator:
    def __init__(self, num):
        self.number=num

    def square(self):
        print(f"the square of{self.number} is {self.number**2}")

    def cube(self):
        print(f"the cube of{self.number} is {self.number**3}")

    def sqroot(self):
        print(f"the square root of{self.number} is {self.number**0.5}")
N = Calculator(9)

N.square()
N.cube()
N.sqroot()