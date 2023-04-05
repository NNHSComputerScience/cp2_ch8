
# Private Critter
# Demonstrates private attributes and private methods
#   To encourage encapsulation, you can define attributes or methods as 'private',
#   meaning only other methods of the object can easily access or invoke it.
#   However, privacy is only a convention in Pyhton; there is no true privacy
#   as in other languages

class Critter(object):
    """A virtual pet"""
    def __init__(self, name): 
        """constructor for Critter class"""
        print ("A new critter has been born!")
        self.name = name
        

    def get_name(self):
        """returns Critter name"""
        return self.name

def main():
    crit = Critter("Poochie")
    
    print("\nAccessing private attributes:")
    
    
    print("\nCalling private methods")


main()
input("\n\nPress the enter key to exit.")
Displaying private_critter_starter.py.
