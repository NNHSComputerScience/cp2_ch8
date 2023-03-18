# Critter example class
#   Critter attributes: name, color, mood
#   Critter methods: talk, getters/setters

class Critter:
  """A virtual pet"""
  def __init__(self, i_name, i_color = "yellow", i_mood = "happy"): 
    """initializes a Critter object with a name, color, and mood"""
    self._name = i_name
    self._color = i_color
    self._mood = i_mood
    
  def talk(self, message):  
    """makes a Critter talk by printing a message"""
    print(message)

  def get_name(self):
    """returns the Critter's name"""
    return self._name 

  def set_name(self, new_name):
    """changes the name of a Critter"""
    self._name = new_name 
        
  def get_color(self):
    """returns the Critter's color"""
    return self._color
        
  def set_color(self, new_color):
    """assigns the Critter a new color"""
    self._color = new_color
    
  def get_mood(self):
    """returns a Critter's current mood"""
    return self._mood

  def set_mood(self, new_mood):
    """changes a Critter's mood"""
    self._mood = new_mood

  def __str__(self):
    """String representation of a Critter object"""
    string = "\nCritter:"
    string += "\nName: " + self._name
    string += "\nColor: " + self._color
    string += "\nMood: " + self._mood
    return string
