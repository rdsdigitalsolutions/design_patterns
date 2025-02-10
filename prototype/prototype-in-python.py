import copy

class GameCharacter:
    def __init__(self, name, level, skills):
        self.name = name
        self.level = level
        self.skills = skills

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Character: {self.name}, Level: {self.level}, Skills: {', '.join(self.skills)}"

# Example Usage
character1 = GameCharacter("Hero", 10, ["Sword Mastery", "Shield Block"])
character2 = character1.clone()
character2.name = "Dark Hero"
character2.level = 15

print(character1)  # Output: Character: Hero, Level: 10, Skills: Sword Mastery, Shield Block
print(character2)  # Output: Character: Dark Hero, Level: 15, Skills: Sword Mastery, Shield Block
print(character1 == character2) # not the same object;
