import math
x1 = int (input("Enter x1: "))
x2 = int (input("Enter x2: "))
y1 = int (input("Enter y1: "))
y2 = int (input("Enter y2: "))
point1 = (x1, x2)
point2 = (y1, y2)
distance = math.dist(point1, point2)
print ("The distance is: ", distance)
#Reflection
"""
Using a library is more practical than writing all calculations from scratch because it already has built-in functions, significantly reducing the difficulty of coding. If I didn't use a library when doing the formative assessment, I would have to use my own custom logic out of complex mathematical formulas, which would be very complex and tedious for me. It would also make it more time-consuming if I didn't use a library, and I may make more mistakes from my manual approximations, in comparison to using a library, which makes it more precise and optimized with its calculations.
"""