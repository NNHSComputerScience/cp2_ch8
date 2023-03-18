# main function to test out Critter and Critter_zoo classes

# can create multiple classes within one .py file, or import them like this...
from critter import Critter # from critter.py, import class Critter
from critter_zoo import Critter_zoo

def main():
  zoo1 = Critter_zoo("Naperville Critter Zoo") # create zoo
  crit1 = Critter("Poochie") # create Critters
  crit2 = Critter("Randolph", "blue", "sad")
  crit3 = Critter("Louise", "green", "envious")
  zoo1.add_critter(crit1) # add Critters to the zoo
  zoo1.add_critter(crit2)
  zoo1.add_critter(crit3)
  print(zoo1)

  # print each Critter in the zoo
  critter_list = zoo1.get_crits()
  for i in critter_list:
    print(i)

  input("\nPress enter to exit.")

main()