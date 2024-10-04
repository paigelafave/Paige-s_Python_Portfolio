#Lab Week 5
# 2/13/24
# By Paige LaFave
# This is a module containing the functions calculating area of a rectangle, perimeter of a rectangle, area of a circle, and 
    # circumference of a circle. Called in the file "calculationTest.py".


#function: areaOfRectange
def areaOfRectangle(base, height):
    area = base * height # area formula
    str_area = str(area) #convert area to string
    print()
    print()
    print("The area of your rectangle is " + str_area) # print area
    print()
    return str_area

#function: rectanglePerimeter
def rectanglePerimeter(base, height):
    perimeter = 2*(base + height) # perimeter formula
    str_perimeter = str(perimeter) #convert perimeter to string
    print()
    print()
    print("The perimeter of your rectangle is " + str_perimeter) # print perimeter
    print()
    return str_perimeter

#function: areaOfCircle
def areaOfCircle(radius):
    import math
    area = math.pi * (radius**2)
    str_area = str(area) #convert area to string
    print()
    print()
    print("The area of your circle is " + str_area) # print area
    print()
    return str_area

#function: cicleCircumference
def circleCircumference(radius):
    import math
    circ = 2 * math.pi * radius
    str_circ = str(circ) #convert circumference to string
    print()
    print()
    print("The circumference of your circle is " + str_circ) # print circumference 
    print()
    return str_circ