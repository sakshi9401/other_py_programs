class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i
    def __add__(self,n1):
        return complex(self.real + n1.real ,self.imaginary + n1.imaginary)

    def __str__():
        return f"{self.real} + {self.imaginary}i"
    
    def __mul__(self,n2):
        pass
c1 = Complex(3,6)
c2 = Complex(5,1)
print(c1 + c2)
#c.add(2,5)
#c.mul(1,4)
