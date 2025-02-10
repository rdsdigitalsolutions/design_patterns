<?php
class GameCharacter {
    private $name;
    private $level;
    private $skills;

    public function __construct($name, $level, $skills) {
        $this->name = $name;
        $this->level = $level;
        $this->skills = $skills;
    }

    public function clone() {
        return clone $this;
    }

    public function setName($name) {
        $this->name = $name;
    }

    public function setLevel($level) {
        $this->level = $level;
    }

    public function __toString() {
        return "Character: {$this->name}, Level: {$this->level}, Skills: " . implode(", ", $this->skills);
    }
}

// Example Usage
$character1 = new GameCharacter("Hero", 10, ["Sword Mastery", "Shield Block"]);
$character2 = $character1->clone();
$character2->setName("Dark Hero");
$character2->setLevel(15);

echo $character1 . "\\n"; // Output: Character: Hero, Level: 10, Skills: Sword Mastery, Shield Block
echo $character2 . "\\n"; // Output: Character: Dark Hero, Level: 15, Skills: Sword Mastery, Shield Block
?>
