class Rectangle:
    def calculateArea(self,lenght,width):
        Area = lenght * width
        print(Area)
    def calcualteParimeter(self,lenght, width):
        perimeter = 2*lenght + 2*width
        print(perimeter)


First = Rectangle()

First.calcualteParimeter(10,5);
First.calculateArea(4,6)