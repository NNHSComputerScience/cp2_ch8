# Unit 3 Notes: Object Oriented Programming
# simple_critter.py
# Description: Demonstrates a basic class and objects. Introduces the constructor method.

# Object Oriented Programming (OOP) - A popular style of programming in which objects are created that contain both data (attributes) and operations (methods).

# OBJECT - A software model that bundles the data (attributes) and operations (methods) relevant for modeling a thing or concept.  
#           An object is created from a CLASS.
# CLASS - A class is a blueprint, or template, for creating software objects. 
#           Custom classes are TYPES, just like Turtles, integer, and strings are types.
#           An object created from a class is an INSTANCE.  

# Defining a Class
#   A user-defined class must be defined using the class keyword before it is used.  
#   Class definitions should include a docstring as the first line of the class definition.  
#   The scope of a class is defined using indentation, much like functions.

class Critter:  # class header; class names capitalized by convention
    """A virtual pet""" # docstring to describe class

    # CONSTRUCTOR - Every class should have a method with the special name __init__. 
    #   This initializer method, often referred to as the constructor, is a special method that is automatically called whenever a new instance of a class is created.
    #   It's the method that "constructs" the objects, thus the name.
    def __init__(self):
        """Constructor of the Critter class"""
        print("A new critter has been born!")
        self.age = 0        
        
    # Defining a Method
    # METHODS - written and behave just like a function, except that it is invoked on a specific instance.
    def talk(self): # must have 'self' parameter as a reference to the object.  
    #  The self parameter (you could choose another name, but nobody ever does!) is a variable automatically set to reference the newly-created object. 
    #                   You do not explicitly pass any arguments to the self parameter; it is done implicitly for you.
    #                   Ask yourself - "Which Critter is talking?"
    #                   e.g. If the there is a Critter object named Jerry  
    #                     stored in the reference variable 'jerry', then 'self' 
    #                     is refferring to Jerry when jerry.talk() is executed.
        """Makes the Critter talk"""
        print("\nHi.  I'm an instance of class Critter and I'm", self.age, "years old.")

    # CHALLENGE: Try defining your own sleep() method  and practice calling it!
    def sleep(self):
        """Makes the Critter sleep"""
        print("\nzzzzzz...ZZZZZZZ...zzzzzzz")

def main():
    # creating instances of class Critter
    crit1 = Critter() # crit1 is variable reference to a Critter object
    crit2 = Critter() # a second Critter object is created and referenced
    
    # Now it's easy to create many objects!
    for i in range(500):
        Critter()

    # accessing the methods of our new objects
    crit1.talk()
    crit2.talk()
    crit1.sleep()
    crit2.sleep()

main()
