class Node:
    def __init__(self,subject):
        self.subject = subject
        
        self.nextYes = None
        self.nextNo = None

    def __str__(self) :
        return f"---------------------------------\n"+\
        f"{self.subject}\n\n"+\
        f"Yes--> {self.nextYes}\n"+\
        f"No---> {self.nextNo}\n "+\
        f"----------------------------------------\n"
