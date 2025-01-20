<?php

class Singleton
{
    private static ?Singleton $instance = null; // Nullable static property to store the instance.
    private ?string $value; // Nullable property to store the value.

    // Private constructor to prevent direct instantiation.
    private function __construct(?string $value = null)
    {
        $this->value = $value;
    }

    // Static method to get or create the single instance.
    public static function getInstance(?string $value = null): Singleton
    {
        if (self::$instance === null) {
            echo "Creating a new instance of Singleton.\n";
            self::$instance = new Singleton($value);
        }
        return self::$instance;
    }

    // Getter for the value.
    public function getValue(): ?string
    {
        return $this->value;
    }

    // Setter for the value.
    public function setValue(string $value): void
    {
        $this->value = $value;
    }
}

// Demonstrating the Singleton pattern.
$singleton1 = Singleton::getInstance("Original Class");

$instances = [];

echo "\nHere I try to create more instances (singleton):\n";
for ($i = 0; $i < 5; $i++) {
    $newClass = Singleton::getInstance("Second Instance"); // Value won't change after the first creation.
    $instances[] = $newClass;
    echo "New Class Value: " . $instances[$i]->getValue() . ", Singleton Class Value: " . $singleton1->getValue() . ". Loop #{$i}\n";
}

// Demonstrate that all instances refer to the same Singleton.
$instances[2]?->setValue("Something else");

echo "\nThis demonstrates that both references point to the same instance:\n";
echo "Is '{$instances[2]?->getValue()}' == '{$instances[1]?->getValue()}'? " . ($instances[2]?->getValue() === $instances[1]?->getValue() ? 'Yes' : 'No') . "\n";
echo "Is '{$instances[1]?->getValue()}' == '{$instances[3]?->getValue()}'? " . ($instances[1]?->getValue() === $instances[3]?->getValue() ? 'Yes' : 'No') . "\n";
echo "Is '{$singleton1->getValue()}' == '{$instances[3]?->getValue()}'? " . ($singleton1->getValue() === $instances[3]?->getValue() ? 'Yes' : 'No') . "\n";

?>
