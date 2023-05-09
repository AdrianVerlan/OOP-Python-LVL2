 
class Box:
    def __init__(self,content):
        if content != None:
            self.__content=content
        else:
            print("Error! None cannot be in the box")

    def __str__(self):
        return f"BOX [{self.__content}]"
    

b1= Box("A good music")
b2= Box("A good book")

b1.__content= None
print(b1)
print(b2)