# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call base class constructor
        self.storage = storage
        self.battery = battery

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"🔋 Battery charged to {self.battery}%")

    def use_storage(self, amount):
        if amount <= self.storage:
            self.storage -= amount
            print(f"📦 {amount}GB used, {self.storage}GB left")
        else:
            print("❌ Not enough storage!")

