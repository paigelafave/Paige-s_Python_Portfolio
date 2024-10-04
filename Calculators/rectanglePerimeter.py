#function: rectanglePerimeter
def rectanglePerimeter(base, height):
    perimeter = 2*(base + height) # perimeter formula
    str_perimeter = str(perimeter) #convert perimeter to string
    print("The perimeter of your rectangle is " + str_perimeter) # print perimeter
    print()
    return str_perimeter


#input and print answer function as main
def main():
    # Lab Week 5
    #rectanglePerimeter.py
    #By: Paige LaFave
    # Created 2/13/24
    # This code will prompt a user for the length and height of a rectangle from a function. Then calculate and print out the perimeter
        # using another function, which can be called using a different script. 
    #Formula info:
        #https://byjus.com/maths/perimeter-of-rectangle/
    # Author: BYJUS, no date created, accessed 1/31/24
    print()
    base = float(input("Please enter the base length of your rectangle: ")) #input of base
    print()
    height = float(input("Please enter the height of your rectangle: ")) #input of height
    print()
    answer = rectanglePerimeter(base, height)
    return answer

if __name__ == "__main__":
    main()