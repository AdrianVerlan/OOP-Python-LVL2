class Cabinet():
    def __init__(self):
        self.top = None
        self.middle = None
        self.bottom = None

    def putOn(self, shelfName, thing):
        shelf = getattr(self, shelfName)
        if shelf is None or shelf == " " * 26:
            setattr(self, shelfName, thing)
        elif shelf is not None:
            print(f"{shelfName} shelf is not empty! Cannot place {thing} on it.")
        else:
            print(f"Cannot place {thing} on {shelfName} shelf, it does not exist!")

    def takeFrom(self, shelfName):
        shelf = getattr(self, shelfName)
        if shelf is None:
            print(f"Nothing to take! The {shelfName} shelf is empty.")
        else:
            setattr(self, shelfName, None)
            return shelf

    def printSchema(self):
        topShelf = self.top if self.top is not None else " " * 26
        middleShelf = self.middle if self.middle is not None else " " * 26
        bottomShelf = self.bottom if self.bottom is not None else " " * 26

        print("##############################")
        print(f"# {topShelf:^26} #")
        print("##############################")
        print(f"# {middleShelf:^26} #")
        print("##############################")
        print(f"# {bottomShelf:^26} #")
        print("##############################")


cabinet = Cabinet()
cabinet.putOn('top', 'o vaza')
cabinet.putOn('middle', 'o carte')
cabinet.printSchema()
