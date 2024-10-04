#function: areaOfRectange
def areaOfRectangle(base, height):
    area = base * height # area formula
    str_area = str(area) #convert area to string
    print("The area of your rectangle is " + str_area) # print area
    print()
    return str_area


#input and print answer function as main
def main():
    # Lab Week 5
    #areaOfRectangle.py
    #By: Paige LaFave
    # Created 2/13/24
    # This code will prompt a user for the length and height of a rectangle in a function. Then, using another function, will calculate
        # and print out the area, which can be called from another script.
    #Formula info:
        # https://www.splashlearn.com/math-vocabulary/measurements/area-of-rectangle-formula
    # Author: SplashLearn, no date created
    print()
    base = float(input("Please enter the base length of your rectangle: ")) #input of base
    print()
    height = float(input("Please enter the height of your rectangle: ")) #input of height
    print()
    answer = areaOfRectangle(base, height)
    return answer

if __name__ == "__main__":
    main()