class Singleton:
    
    _instance = None  # This is a class-level attribute to store the single instance of the class.

    def __new__(cls, *args, **kwargs):
        """
        Overrides the default __new__ method to control the instance creation.
        """
        if cls._instance is None:
            # If no instance exists, create one and store it in _instance.
            cls._instance = super().__new__(cls)  # Pass only the class itself.
            print("\nCreating a new instance of Singleton.")
        
        return cls._instance

    def __init__(self, value=None):
        """
        The initializer method sets the value. If it's already set, it doesn't reset it.
        """
        if not hasattr(self, 'value'):
            # Initialise the 'value' attribute only once.
            self.value = value
    
    def __str__(self):
        return self.value

def check_is_same(instances):
    """
    Simple function to check if it's singleton.
    """

    print("\nShows they are all the same class:\n")

    for i in range(len(instances)):
        if instances[i] is singleton1:
            print(f"Instance #{i} is '{instances[2].value}'!")
        else:
            print(f"Instance #{i} is not singleton!!!")

if __name__ == "__main__":
    """
    Demonstrating the Singleton pattern.
    """
    
    # Creates the first instace.
    singleton1 = Singleton("Original Class")
    instances = []
    
    for i in range(5):
        new_class = Singleton("Second Instance") # No matter the name, it will not be used if the "Singleton" class already exist.
        instances.append(new_class)

    # Here you can see they are all the same class.
    check_is_same(instances)

    # chage the value of one of the instaces to show they all change.
    instances[2].value = "Something else"
    instances[1].value = "Something else 2"
    instances[3].value = "Something else 7"

    print("\n\nReferences point to the same instance:\n")
    print(f"Is instance 2 same as instance 1? {instances[2].value==instances[1].value}")
    print(f"Is instance 1 same as instance 3? {instances[1].value==instances[3].value}")
    print(f"Is Original same as instance 3? {singleton1.value==instances[3].value}")

    print("\n\nAll instances are:\n")
    for i in range(len(instances)):
        print(f"Instance #{i} is '{instances[i].value}'!")
