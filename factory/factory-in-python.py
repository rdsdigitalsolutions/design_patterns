# Step 1: Define a base class for Cars
class Car:
    def __init__(self, **kwargs):
        # Set default values
        self.color = "White"
        self.engine = "V4"
        self.doors = 4
        self.tires = 4

        # Create a list of current options
        current_options = [attr for attr, value in self.__dict__.items()]

        # Override default values
        for attr, value in kwargs.items():
            if attr in current_options:
                setattr(self, attr, value)

    def get_properties(self):
        return "\n".join([f"{attr.capitalize()}: {value}" for attr, value in self.__dict__.items()])

    def get_description(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# Step 2: Create concrete car classes
class ElectricCar(Car):
    def get_description(self):
        return f"\n#### Electric Car:\n\nFuel: Electric,\n{self.get_properties()}"

class GasCar(Car):
    def get_description(self):
        return f"\n#### Gas Car:\n\nFuel: Gasoline,\n{self.get_properties()}"

class HybridCar(Car):
    def get_description(self):
        return f"\n#### Hybrid Car:\n\nFuel: Gasoline and Electric,\n{self.get_properties()}"

# Step 3: Create a Factory to generate Cars
class CarFactory:
    @staticmethod
    def create_car(**kwargs):
        match kwargs.get("car_type"):
            case "electric":
                return ElectricCar(**kwargs)
            case "gas":
                return GasCar(**kwargs)
            case "hybrid":
                return HybridCar(**kwargs)
            case _:
                raise ValueError(f"Unknown car type: {car_type}")

# Example usage
def main():
    print("Welcome to the Car Factory!\n")
    
    # Define car specifications
    car_specs = [
        {"car_type": "electric", "color": "red", "engine": "EV-2025", "doors": 2},
        {"car_type": "gas", "color": "blue", "engine": "V8 Turbo"},
        {"car_type": "hybrid", "color": "green", "engine": "EcoBoost-HY", "doors": 2}
    ]

    for spec in car_specs:
        car = CarFactory.create_car(**spec)
        print(car.get_description())

if __name__ == "__main__":
    main()
