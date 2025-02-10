class Burger:
    def __init__(self, size, cheese=False, lettuce=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.lettuce = lettuce
        self.bacon = bacon

    def __str__(self):
        return f"Burger ({self.size}): {'Cheese' if self.cheese else ''} {'Lettuce' if self.lettuce else ''} {'Bacon' if self.bacon else ''}".strip()

class BurgerBuilder:
    def __init__(self, size):
        self.burger = Burger(size)

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_lettuce(self):
        self.burger.lettuce = True
        return self

    def add_bacon(self):
        self.burger.bacon = True
        return self

    def build(self):
        return self.burger

# Example Usage
burger = BurgerBuilder("Large").add_cheese().add_bacon().build()
print(burger)  # Output: Burger (Large): Cheese Bacon
