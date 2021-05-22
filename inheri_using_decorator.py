class Employee:
    salary = 1000
    increament = 2

    @property
    def salaryAfterIncreament(self):
        return self.salary * self.increament

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,val):
        self.increament = val / self.salary

e = Employee()

print(e.salaryAfterIncreament)
e.salaryAfterIncreament = 3000
print(e.increament)