from math import pi

class Circle:
    def __init__(self):
        print("Inside Constructor")
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius: "))
    
    def CalculateArea(self):
        self.Area =  pi * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference =  2 * pi * self.Radius
    
    def Display(self):
        print("The Radius of circle is: ", self.Radius)
        print("The Area of Circle is: ", self.Area)
        print("The Circumference of circle is: ", self.Circumference)
        
    

def main():
    

    object1 = Circle()
    object1.Accept()
    object1.CalculateArea()
    object1.CalculateCircumference()
    object1.Display()

                 

if __name__ == "__main__":
    main()
    

    


