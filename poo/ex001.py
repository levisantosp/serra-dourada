from typing import Literal

VehicleType = Literal["Carro", "Moto"]
VehicleMake = Literal["BMW", "Mercedez", "Toyota", "Ford", "Chevrolet", "Dodge", "Honda", "Yamaha", "Shineray"]

class Vehicle:
        def __init__(
                self,
                type: VehicleType,
                id: int,
                make: VehicleMake,
                model: str,
                year: int
        ):
                self.type = type
                self.id = id
                self.make = make
                self.model = model
                self.year = year
        
        def display(self):
                return f"---------------------------------\nVeículo {self.id}\n\nTipo: {self.type}\nMarca: {self.make}\nModelo: {self.model}\nAno: {self.year}"
        
        def create(self):
                return self

class Car(Vehicle):
        def __init__(self, id: int, make: VehicleMake, model: str, year: int):
                super().__init__(type="Carro", id=id, make=make, model=model, year=year)
                self.id = id
        
class Motorcycle(Vehicle):
        def __init__(self, id: int, make: VehicleMake, model: str, year: int):
                super().__init__(type="Moto", id=id, make=make, model=model, year=year)
                self.id = id

car1 = Car(1, "Ford", "Ranger Raptor", 2025).create()
car2 = Car(2, "Toyota", "Hilux GR-Sport", 2025).create()
car3 = Car(3, "Dodge", "Charger Hellcat", 2023).create()
bike1 = Motorcycle(4, "Honda", "CG 160 Start", 2025).create()
bike2 = Motorcycle(5, "BMW", "G 310 GS", 2019).create()
bike3 = Motorcycle(6, "Yamaha", "MT-07", 2020).create()

vehicles: list[Vehicle] = [
        car1,
        car2,
        car3,
        bike1,
        bike2,
        bike3
]

for vehicle in vehicles:
        print(vehicle.display())