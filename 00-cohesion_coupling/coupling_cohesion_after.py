import string
import random


class VehicleMake:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        return 0.02 if self.electric else 0.05

    def __str__(self):
        return f"Brand: {self.brand}\nPayable Tax: {self.compute_tax()}"


class Vehicle:
    def __init__(self, id_: str, license_plate: str, info: VehicleMake):
        self.id = id_
        self.license_plate = license_plate
        self.info = info

    def __str__(self):
        return f"Id: {self.id}\nLicense plate: {self.license_plate}\n{self.info}"


class VehicleRegistry:
    vehicle_info = {}

    def __init__(self):
        self.add_vehicle_info("Testla Model 3", True, 60_000)
        self.add_vehicle_info("Volkswagen ID3", True, 35_000)
        self.add_vehicle_info("BMW 5", False, 45_000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleMake(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, vehicle_id):
        two_random_digits = ''.join(random.choices(string.digits, k=2))
        two_random_chars = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{vehicle_id[:2]}-{two_random_digits}-{two_random_chars}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Volkswagen ID3")
print(f"Vehicle: {vehicle}")
