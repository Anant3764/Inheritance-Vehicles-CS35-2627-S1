class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def show_info(self):
        print(self.make, self.model)
        print("Speed:", self.speed)


class Car(Vehicle):
    def __init__(self, make, model, speed, doors):
        super().__init__(make, model, speed)
        self.doors = doors

    def show_info(self):
        print("Car:", self.make, self.model)
        print("Speed:", self.speed)
        print("Doors:", self.doors)

    def honk(self):
        print("Car is honking!")


class Motorcycle(Vehicle):
    def __init__(self, make, model, speed, has_sidecar):
        super().__init__(make, model, speed)
        self.has_sidecar = has_sidecar

    def show_info(self):
        print("Motorcycle:", self.make, self.model)
        print("Speed:", self.speed)
        print("Has sidecar:", self.has_sidecar)

    def wheelie(self):
        print("Motorcycle is doing a wheelie!")