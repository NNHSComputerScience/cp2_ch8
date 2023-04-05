
# Classy Critter
# Demonstrates class attributes and static methods

class Critter:
    """A virtual pet"""
    # CLASS ATTRIBUTE (CLASS VARIABLE) - a variable that does not belong to one object, but the entire class.
    total = 0 
        
    def __init__(self, name):
        """Initializes a Critter's attributes"""
        print("A critter has been born!")
        self.name = name
        Critter.total += 1
        
    # STATIC METHOD - a special type of method that belongs to the class, and not to any individual object.
    @staticmethod # decorator that modifies the following method to restrict object access
    def status(): # no 'self' required since this method does not belong to a specific object
        """Prints the total number of Critter objects"""
        print("\nThe total number of critters is", Critter.total)

def main():
    print("Accessing the class attribute Critter.total:", end=" ")
    print(Critter.total) # class attributes can be accessed before an object is created

    print("\nCreating critters.")
    crit1 = Critter("critter 1")
    crit2 = Critter("critter 2")
    crit3 = Critter("critter 3")

    print("\nInvoking the static method...")
    Critter.status()

    print("\nAccessing the class attribute through an object:", end= " ")
    print(crit1.total)  # you cannot change the class attribute with this syntax

main()
classy_critter_finished.py
Displaying classy_critter_finished.py.
