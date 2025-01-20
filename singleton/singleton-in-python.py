class Singleton:
    
    _instance = None  # This is a class-level attribute to store the single instance of the class.

    def __new__(cls, *args, **kwargs):
        """
        Overrides the default __new__ method to control the instance creation.
        """
        if cls._instance is None:
            # If no instance exists, create one and store it in _instance.
            cls._instance = super().__new__(cls)  # Pass only the class itself.
            print("Creating a new instance of Singleton.\n")
        
        return cls._instance

    def __init__(self, value=None):
        """
        The initializer method sets the value. If it's already set, it doesn't reset it.
        """
        if not hasattr(self, 'value'):
            # Initialise the 'value' attribute only once.
            self.value = value

def check_is_same(instances):
    """
    Simple function to check if it's singleton.
    """

    print("\n\nHere you can see they are all the same class.")

    for i in range(len(instances)):
        if instances[i] is singleton1:
            print(f"Instance #{i} is singleton!")
        else:
            print(f"Instance #{i} is not singleton!!!")

if __name__ == "__main__":
    """
    Demonstrating the Singleton pattern.
    """
    
    # Creates the first instace.
    singleton1 = Singleton("Original Class")
    instances = []

    
    print("\nHere I try to create more instances (singleton)")
    for i in range(5):
        new_class = Singleton("Second Instance") # No matter the name, it will not be used if the "Singleton" class already exist.
        instances.append(new_class)
        print(f"New Class Name: {instances[i].value}, Singleton Class name: {singleton1.value}. Loop #{i}")

    # Here you can see they are all the same class.
    check_is_same(instances)

    # chage the value of one of the instaces to show they all change.
    instances[2].value = "Something else"

    print("\n\nThis demonstrates that both references point to the same instance.")
    print(f"Is {instances[2].value} == {instances[1].value}? {instances[2].value==instances[1].value}")
    print(f"Is {instances[1].value} == {instances[3].value}? {instances[1].value==instances[3].value}")
    print(f"Is {singleton1.value} == {instances[3].value}? {singleton1.value==instances[3].value}")
