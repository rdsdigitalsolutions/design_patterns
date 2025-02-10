class GameCharacter {
    constructor(name, level, skills) {
        this.name = name;
        this.level = level;
        this.skills = skills;
    }

    clone() {
        return new GameCharacter(this.name, this.level, [...this.skills]);
    }

    toString() {
        return `Character: ${this.name}, Level: ${this.level}, Skills: ${this.skills.join(", ")}`;
    }
}

// Example Usage
const character1 = new GameCharacter("Hero", 10, ["Sword Mastery", "Shield Block"]);
const character2 = character1.clone();
character2.name = "Dark Hero";
character2.level = 15;

console.log(character1.toString()); // Output: Character: Hero, Level: 10, Skills: Sword Mastery, Shield Block
console.log(character2.toString()); // Output: Character: Dark Hero, Level: 15, Skills: Sword Mastery, Shield Block
