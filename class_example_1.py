class Programmer:
    company = "microsoft"

    def __init__(self,name, product):
        self.name = name
        self.product=product
    
    def getInfo(self):
        print(f"the name of employee of the company {self.company} is {self.name} and the product is {self.product}")

sakshi = Programmer("sakshi", "HackerRank")
mahima = Programmer("mahima","GitHub")
sakshi.getInfo()
mahima.getInfo()