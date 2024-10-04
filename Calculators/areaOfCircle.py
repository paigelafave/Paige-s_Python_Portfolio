#function: areaOfCircle
def areaOfCircle(radius):
    import math
    area = math.pi * (radius**2)
    str_area = str(area) #convert area to string
    print()
    print("The area of your circle is " + str_area) # print area
    print()
    return str_area


#input and print answer function as main
def main():
    # Lab Week 5
    #areaOfCircle.py
    #By: Paige LaFave
    # Created 2/13/24
    # This code will prompt the user for a radius in a function and calculate and print out the area of the circle using another function,
        # which can be called using another script.
    #Formula info:
        #https://www.cuemath.com/geometry/area-of-a-circle/
    #Author: CUEMATH, no date created\
    print()
    radius = float(input("Please enter the radius of your circle: "))#input of radius
    answer = areaOfCircle(radius)
    return answer

if __name__ == "__main__":
    main()