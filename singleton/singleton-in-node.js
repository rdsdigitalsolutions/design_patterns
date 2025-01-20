class Singleton {
    // Private static property to hold the instance
    static #instance = null;

    constructor(value = null) {
        if (Singleton.#instance) {
            throw new Error("Use Singleton.getInstance() to get the instance.");
        }
        this.value = value;
        Singleton.#instance = this;
        console.log("Creating a new instance of Singleton.");
    }

    // Static method to get the single instance
    static getInstance(value = null) {
        if (Singleton.#instance === null) {
            Singleton.#instance = new Singleton(value);
        }
        return Singleton.#instance;
    }

    // Method to get the value
    getValue() {
        return this.value;
    }

    // Method to set the value
    setValue(value) {
        this.value = value;
    }
}

// Demonstrating the Singleton pattern
const singleton1 = Singleton.getInstance("Original Class");

const instances = [];
console.log("\nHere I try to create more instances (singleton):");
for (let i = 0; i < 5; i++) {
    const newClass = Singleton.getInstance("Second Instance"); // Value won't change after the first creation
    instances.push(newClass);
    console.log(
        `New Class Value: ${instances[i].getValue()}, Singleton Class Value: ${singleton1.getValue()}. Loop #${i}`
    );
}

// Demonstrate that all instances refer to the same Singleton
instances[2].setValue("Something else");

console.log("\nThis demonstrates that both references point to the same instance:");
console.log(
    `Is '${instances[2].getValue()}' == '${instances[1].getValue()}'? ${instances[2].getValue() === instances[1].getValue() ? "Yes" : "No"
    }`
);
console.log(
    `Is '${instances[1].getValue()}' == '${instances[3].getValue()}'? ${instances[1].getValue() === instances[3].getValue() ? "Yes" : "No"
    }`
);
console.log(
    `Is '${singleton1.getValue()}' == '${instances[3].getValue()}'? ${singleton1.getValue() === instances[3].getValue() ? "Yes" : "No"
    }`
);
