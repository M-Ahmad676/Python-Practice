# instance attribute and Class attributes

class Car:
    def __init__(self, year,make,model):
        self.year = year
        self.make = make
        self.model = model
    
    def start_engine(self):
        print(f"Activating Engine {self.make} {self.model} has started ")


c1 = Car(2012, "Honda", "Accord")
c1.start_engine()