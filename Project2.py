# Project 2:
# Write a program that calculates the number of packages of hot dogs and the 
# number of packages of hot dog buns needed for a cookout, with the minimum 
# amount of leftovers.

# The program should ask the user for the number of people attending the 
# cookout and the number of hot dogs each person will be given.

# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

# The program should display the following details:

# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over


def ceilDiv(a,b):
    '''
    Function: Calculates ceiling division of two inputs
    Inputs:   int/float
    Outputs:  int
    '''
    return (-a // b) * -1
      
def dogsAndBuns(people_attending, hotdogs_per_person):
    '''
    Function: Calculates number of packages of hot dogs and buns
              needed with minimum amt of leftovers
    Inputs:   number of people attending, int
              number of hotdogs per person, int
    Outputs:  number of hot dog packages required, int
              number of bun packages required, int
              number of hot dogs left over, int
              number of buns left over, int
    '''
    #initialize variables
    DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8
    attendees = people_attending
    dogsPerPerson = hotdogs_per_person

    #formulas
    dogsNeeded = attendees * dogsPerPerson
    bunsNeeded = dogsNeeded    
    dogPkgNeeded = ceilDiv(dogsNeeded,DOGS_PER_PACKAGE)
    dogsBought = dogPkgNeeded * DOGS_PER_PACKAGE
    dogsLeft = dogsBought - dogsNeeded
    bunPkgNeeded = ceilDiv(bunsNeeded,BUNS_PER_PACKAGE)
    bunsBought = bunPkgNeeded * BUNS_PER_PACKAGE
    bunsLeft = bunsBought - bunsNeeded

    #output
    print("\nPackages Needed:")
    print("----------------")
    print(f'hotdog pkgs needed: {dogPkgNeeded} ({dogsBought} total hot dogs with {dogsLeft} hot dogs leftover)')
    print(f'   bun pkgs needed: {bunPkgNeeded} ({bunsBought} total buns with {bunsLeft} buns leftover)')

def main():
    while True:
      try:
        NumPeople = int(input("Number of people attending cookout: "))
        DogsPerPerson = int(input("Number of hot dogs each person will be given: "))
        break
      except:
        print("Please enter a valid number.")
        continue
    dogsAndBuns(NumPeople, DogsPerPerson)

#main
if __name__ == "__main__":
  main()
