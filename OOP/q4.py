import math
class Shape:
    def cal_area(self):
        pass

    def cal_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius

    def cal_area(self):
        return math.pi * (self.radius ** 2)
    
    def cal_perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def cal_area(self):
        return (self.length * self.breadth)
    
    def cal_perimeter(self):
        return 2*(self.length + self.breadth)
    
class Triangle(Shape):
    def __init__(self,base,height,side1,side2,side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def cal_area(self):
        return (0.5 * self.base * self.height)
    
    def cal_perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    

def main():
    while True:
        print("Choose a shape to calculate the area and perimeter: ")
        print("1.Circle")
        print("2.Rectangle")
        print("3.Triangle")
        print("4.Exit")

        choice = int(input("Enter your choice(1-4):"))

        if choice == 1:
            r = float(input("Enter the radius of the circle: "))
            shape = Circle(r)
        elif choice == 2:
            l = float(input("Enter the length of the rectangle: "))
            b = float(input("Enter the breadth of the rectangle: "))
            shape = Rectangle(l,b)
        elif choice == 3:
            b = float(input("Enter the base: ")) 
            h = float(input("Enter the height: "))
            s1 = float(input("Enter the side1: "))
            s2 = float(input("Enter the side2: ")) 
            s3 = float(input("Enter the side3: "))
            shape = Triangle(b,h,s1,s2,s3)
        elif choice == 4:
            print("Exiting the program")
            break
        else:
            print("Invalid Choice")
            continue

        print(f"Area: {shape.cal_area()}")
        print(f"perimeter: {shape.cal_perimeter()}")
        print()

if __name__ == "__main__":
    main()

