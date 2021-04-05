# GetSet Critter
# Demonstrates using getter and setter methods to access 
#   and assign attribute values

# CHALLENGE: Write a class Critter such that Critters have custom names. Also,
#               provide a method which allows Critters to print thier name and
#               a String method.

class Critter:
    """A virtual pet"""
    def __init__(self, name): 
        """constructor of class Critter"""
        self.name = name
        self.color = "turquoise"
    
    # not a GETTER method; in general, avoid printing in functions/methods
    #   if possible. rather, write a get method and let the printing happen
    #   elsewhere.
    def talk(self):
        """makes Critter talk and say its name"""
        print("\nHi, I'm", self.name)

    def get_name(self):  # GETTER: accessor method to GET(return) an attribute
        """returns the Critter's name"""
        return self.name 

    def set_name(self, new_name = ""): # SETTER: mutator method to SET(reassign) an attribute to a new value
        """changes the name of a Critter"""
        if new_name and isinstance(new_name, str): 
            self.name = new_name 
        else:
            print("A Critter's name must be a non-empty string.")
        
    # CHALLENGE: Create a second attribute called color and create getter and
    #           setter methods for the color attribute.  Use them in the main.
    def get_color(self):
        """returns the Critter's color"""
        return self.color
        
    def set_color(self, new_color):
        """assigns the Critter a new color"""
        if new_color and isinstance(new_color, str): # isinstance checks if an object(instance) is of a certain type
            self.color = new_color
        else:
            print("You must provide a color string in order to change the color.")
    
    def __str__(self):
        """String method for a Critter object"""
        string = "\nCritter:"
        string += "\nName: " + self.name
        string += "\nColor: " + self.color
        return string

def main():
    crit = Critter("Poochie")
    crit.talk()

    print("\nMy Critter's name is: ", end="")
    print(crit.get_name())
    print("\nChanging my Critter's name...")
    crit.set_name("Randolph") 
    # Note: Critter objects are MUTABLE (as are most objects), meaning their attributes can be changed.
    #   That means we don't have to reassign to the 'crit' variable like this:
    #       crit = crit.set_name("Randolph")
    # Which objects have we used that are NOT mutable?
    print(f"The Critter's name is changed to {crit.get_name()}.")
    
    # color testing
    print(f"{crit.get_name()} is {crit.get_color()}")
    crit.set_color("tangerine orange")
    print(f"{crit.get_name()} is {crit.get_color()}.")
     
main()
input("\n\nPress the enter key to exit.") 
