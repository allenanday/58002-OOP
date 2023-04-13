class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.pi = 3.1416

    def perimeter(self):
        return 2 * self.pi * self.diameter

    def area(self):
        return self.pi * self.diameter ** 2

    def display(self):
        print("The perimeter of the circle is:", self.perimeter())
        print("The area of the circle is:", self.area())

circle = Circle(float(input("Insert a value of Diameter: ")))
circle.display()
