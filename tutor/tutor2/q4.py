class Square(object):
    def __init__(self, theLength = 2):
        self.length = theLength

    def getLength(self):
        return self.length

    def setLength(self, theLength):
        self.length = theLength

    def area(self):
        return self.getLength()**2
        
    # print the square length 
    def outputLength(self):
        print("The length is " +str(self.length))

    # print the area and perimeter 
    def printAP(self):
        print(f'The area is {self.area()}')
        print(f'The perimeter is {self.length * 4}')

g = Square()
h = Square(5)
g.outputLength()
g.printAP()
h.outputLength()
h.printAP()
print("The length is " + str(h.getLength()))
h.setLength(4)
print("The length is now " + str(h.getLength()))


