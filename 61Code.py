class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def __repr__(self):
        return f"Car(brand ={self.brand},speed={self.speed})"

car = Car("BMW",200)
print(repr(car))    