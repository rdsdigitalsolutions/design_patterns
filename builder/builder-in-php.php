<?php
class Burger {
    private $size;
    private $cheese = false;
    private $lettuce = false;
    private $bacon = false;

    public function __construct($size) {
        $this->size = $size;
    }

    public function addCheese() {
        $this->cheese = true;
        return $this;
    }

    public function addLettuce() {
        $this->lettuce = true;
        return $this;
    }

    public function addBacon() {
        $this->bacon = true;
        return $this;
    }

    public function build() {
        return $this;
    }

    public function __toString() {
        return "Burger ({$this->size}): " . 
               ($this->cheese ? "Cheese " : "") . 
               ($this->lettuce ? "Lettuce " : "") . 
               ($this->bacon ? "Bacon " : "");
    }
}

// Example Usage
$burger = (new Burger("Large"))->addCheese()->addBacon()->build();
echo $burger; // Output: Burger (Large): Cheese Bacon
?>
