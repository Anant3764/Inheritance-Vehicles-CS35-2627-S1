from vehicles import Vehicle, Car, Motorcycle

car = Car("Toyota", "Camry", 180, 4)
motorcycle = Motorcycle("Honda", "CBR", 220, False)

print("CAR")
car.show_info()
car.honk()

print("MOTORCYCLE")
motorcycle.show_info()
motorcycle.wheelie()