class IStream:
    
    def __init__(self) :
        self.buffer = None

    def read(self,data):
        self.buffer = data
    
    def __lshift__(self, data):
        self.buffer = data







is_ = IStream()
sourse = 10_000_000

is_ << sourse

if is_.buffer > 5_000_000:
    print("low traffic")
else:
    print("hight traffic")

#print("before", is_.buffer)
#is_.read("abcdef")
#print("after", is_.buffer)
