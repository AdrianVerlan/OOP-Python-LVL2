class Dog:
    pass
def createDog(name,race,year,allive):
    dog=Dog()
    dog.name   = name
    dog.race   = race
    dog.year   = year
    dog.allive = allive
    return dog

def printDog(dog):
    print()
    print(dog.name)
    print(dog.race)
    print(dog.year)
    print(dog.allive)

my_dog =  createDog("Mufasa", "Cane Corso" ,2012 ,True)
printDog(my_dog)
your_dog = createDog("Sharic","Buldog", 2200, True)
printDog(your_dog)