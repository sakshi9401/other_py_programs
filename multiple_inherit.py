class Animal:
    category = "mammal"

class Pet(Animal):
    color = "white"
    def petCategory(self):
        print(f"the category of pet is dog")

class Dog(Pet):
    def bark(self):
        super().petCategory()
        print("I am dog")

d = Dog()
d.bark()
print(f"I am {d.color} in colour")
p = Pet()
#p.petCategory()
a = Animal()
print(f"I am a {a.category}")

