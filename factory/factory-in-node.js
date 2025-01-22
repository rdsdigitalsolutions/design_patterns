// Step 1: Define a base class for Cars
class Car {
    constructor({ color = "White", engine = "V4", doors = 4, tires = 4 } = {}) {
        this.color = color;
        this.engine = engine;
        this.doors = doors;
        this.tires = tires;
    }

    getProperties() {
        return Object.entries(this)
            .map(([key, value]) => `${key.charAt(0).toUpperCase() + key.slice(1)}: ${value}`)
            .join("\n");
    }

    getDescription() {
        throw new Error("This method should be implemented by subclasses.");
    }
}

// Step 2: Create concrete car classes
class ElectricCar extends Car {
    getDescription() {
        return `\n#### Electric Car:\n\nFuel: Electric,\n${this.getProperties()}`;
    }
}

class GasCar extends Car {
    getDescription() {
        return `\n#### Gas Car:\n\nFuel: Gasoline,\n${this.getProperties()}`;
    }
}

class HybridCar extends Car {
    getDescription() {
        return `\n#### Hybrid Car:\n\nFuel: Gasoline and Electric,\n${this.getProperties()}`;
    }
}

// Step 3: Create a Factory to generate Cars
class CarFactory {
    static createCar({ car_type, ...params }) {
        switch (car_type) {
            case "electric":
                return new ElectricCar(params);
            case "gas":
                return new GasCar(params);
            case "hybrid":
                return new HybridCar(params);
            default:
                throw new Error(`Unknown car type: ${car_type}`);
        }
    }
}

// Example usage
function main() {
    console.log("Welcome to the Car Factory!\n");

    // Define car specifications
    const carSpecs = [
        { car_type: "electric", color: "red", engine: "EV-2025", doors: 2 },
        { car_type: "gas", color: "blue", engine: "V8 Turbo" },
        { car_type: "hybrid", color: "green", engine: "EcoBoost-HY", doors: 2 },
    ];

    for (const spec of carSpecs) {
        const car = CarFactory.createCar(spec);
        console.log(car.getDescription());
    }
}

main();
