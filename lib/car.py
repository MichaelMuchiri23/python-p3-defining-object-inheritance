from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


#Case example
ferrari = Car(1, 5)
print(ferrari.go())
porsche = Vehicle(1, 5)
print(porsche.go())
