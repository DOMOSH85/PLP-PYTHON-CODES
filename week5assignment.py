# This code defines a base class `Superhero` and a derived class `FlyingSuperhero`.
# The `Superhero` class has attributes for name, power, and city, and methods to display information and use powers.


class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        return f"{self.name} fights crime in {self.city} with the power of {self.power}."

    def use_power(self):
        return f"{self.name} uses their {self.power}!"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def display_info(self):
        return super().display_info() + f" They can fly at a speed of {self.flight_speed} km/h."

    def use_power(self):
        return super().use_power() + f" They soar through the skies!"

# Example usage
hero1 = Superhero("Captain Valor", "super strength", "Metropolis")
hero2 = FlyingSuperhero("Sky Guardian", "flight", "Gotham", 150)

print(hero1.display_info())
print(hero1.use_power())
print(hero2.display_info())
print(hero2.use_power())






# This code defines a base class `Vehicle` and derived classes `Car`, `Plane`, and `Bicycle`.
# Each derived class implements the `move` method to return a string indicating how the vehicle moves.
# The `test_vehicle_movement` function takes a list of vehicles and prints their movement.
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

# Example usage
def test_vehicle_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())

# Creating instances of each vehicle
car = Car()
plane = Plane()
bicycle = Bicycle()

# Testing the movement of different vehicles
test_vehicle_movement([car, plane, bicycle])