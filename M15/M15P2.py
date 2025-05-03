
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Sticker Price: ${self.sticker_price:,.2f}")
        print(f"Discount Price: ${self.discount_price():,.2f}")


class Sportcar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.option_wheels = 'N'
        self.option_engine = 'N'
        self.option_interior = 'N'

    def SportWheels(self, value):
        self.option_wheels = value.upper()

    def SportEngine(self, value):
        self.option_engine = value.upper()

    def SportInterior(self, value):
        self.option_interior = value.upper()

    def updated_price(self):
        base_price = self.discount_price()
        if self.option_wheels == 'Y':
            base_price += 1000.00
        if self.option_engine == 'Y':
            base_price += 3000.00
        if self.option_interior == 'Y':
            base_price += 2000.00
        return base_price

    def display_info(self):
        super().display_info()
        print(f"Updated Price (with options): ${self.updated_price():,.2f}")


print("== Regular Cars ==")
car1 = Car("Toyota", "Camry", 25000)
car1.display_info()
print()

car2 = Car("Honda", "Civic", 23000)
car2.display_info()
print()


print("== Sportcars ==")
sport1 = Sportcar("Chevy", "Corvette", 60000)
sport1.SportWheels('Y')
sport1.SportEngine('N')
sport1.SportInterior('Y')
sport1.display_info()
print()

sport2 = Sportcar("Ford", "Mustang", 55000)
sport2.SportWheels('Y')
sport2.SportEngine('Y')
sport2.SportInterior('Y')
sport2.display_info()
