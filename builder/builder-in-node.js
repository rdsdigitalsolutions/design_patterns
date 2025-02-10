class Burger {
    constructor(size) {
        this.size = size;
        this.cheese = false;
        this.lettuce = false;
        this.bacon = false;
    }

    addCheese() {
        this.cheese = true;
        return this;
    }

    addLettuce() {
        this.lettuce = true;
        return this;
    }

    addBacon() {
        this.bacon = true;
        return this;
    }

    build() {
        return this;
    }

    toString() {
        return `Burger (${this.size}): ${this.cheese ? "Cheese " : ""}${this.lettuce ? "Lettuce " : ""}${this.bacon ? "Bacon " : ""}`.trim();
    }
}

// Example Usage
const burger = new Burger("Large").addCheese().addBacon().build();
console.log(burger.toString()); // Output: Burger (Large): Cheese Bacon
