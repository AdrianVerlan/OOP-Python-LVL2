class cInt():
    def __init__(self, value):
        if value < -999 or value >999:
            raise ValueError("Value must be between -999 and 999.")
        self.value = value

    def __str__(self):
        return f"{self.value}"
    
    def __sub__(self, other):
        return int(self.value - other.value)
    
    def __add__ (self, other):
        return int(self.value + other.value)
    
    def __truediv__(self, other):
        return int(self.value / other.value)
    
    def __mul__(self, other):
        return int(self.value * other.value)
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self,other):
        return self.value == other.value
    
    def __gt__(self,other):
        return self.value > other.value
    
    







a = cInt(100)
b = cInt(20)
r = a - 10
print(r)        