class DOG:
    def __init__(self,name,race,year,allive):
        self.name = name
        self.race = race
        self.year = year
        self.allive = allive
    
    def printDog(self):
        print(self.name)
        print(self.race)
        print(self.year)
        print(self.allive)

#step2 use

my_dog = DOG("Tuzic", "Cane Corso", 2010, True)
my_dog.printDog()

print()

friends_dog = DOG ("Sharic", "Buldog", 2020, True)
friends_dog.printDog()