<?php

// Step 1: Define a base class for Cars
abstract class Car {
    protected $color = "White";
    protected $engine = "V4";
    protected $doors = 4;
    protected $tires = 4;

    public function __construct(array $arguments = []) {
        $currentOptions = array_keys(get_object_vars($this));
        
        foreach ($arguments as $key => $value) {
            if (in_array($key, $currentOptions)) {
                $this->$key = $value;
            }
        }
    }

    public function getProperties(): string {
        $properties = "";
        foreach (get_object_vars($this) as $key => $value) {
            $properties .= ucfirst($key) . ": $value\n";
        }
        return $properties;
    }

    abstract public function getDescription(): string;
}

// Step 2: Create concrete car classes
class ElectricCar extends Car {
    public function getDescription(): string {
        return "\n#### Electric Car:\n\nFuel: Electric,\n" . $this->getProperties();
    }
}

class GasCar extends Car {
    public function getDescription(): string {
        return "\n#### Gas Car:\n\nFuel: Gasoline,\n" . $this->getProperties();
    }
}

class HybridCar extends Car {
    public function getDescription(): string {
        return "\n#### Hybrid Car:\n\nFuel: Gasoline and Electric,\n" . $this->getProperties();
    }
}

// Step 3: Create a Factory to generate Cars
class CarFactory {
    public static function createCar(array $arguments): Car {
        switch ($arguments['car_type'] ?? '') {
            case "electric":
                return new ElectricCar($arguments);
            case "gas":
                return new GasCar($arguments);
            case "hybrid":
                return new HybridCar($arguments);
            default:
                throw new InvalidArgumentException("Unknown car type: " . ($arguments['car_type'] ?? 'null'));
        }
    }
}

// Example usage
function main() {
    echo "Welcome to the Car Factory!\n\n";

    // Define car specifications
    $carSpecs = [
        ["car_type" => "electric", "color" => "red", "engine" => "EV-2025", "doors" => 2],
        ["car_type" => "gas", "color" => "blue", "engine" => "V8 Turbo"],
        ["car_type" => "hybrid", "color" => "green", "engine" => "EcoBoost-HY", "doors" => 2]
    ];

    foreach ($carSpecs as $spec) {
        $car = CarFactory::createCar($spec);
        echo $car->getDescription();
    }
}

main();

?>
