#function: cicleCircumference
def circleCircumference(radius):
    import math
    circ = 2 * math.pi * radius
    str_circ = str(circ) #convert circumference to string
    print()
    print("The circumference of your circle is " + str_circ) # print circumference 
    print()
    return str_circ


#input and print answer function as main
def main():
   # Lab Week 5
    #circleCircumference.py
    #By: Paige LaFave
    # Created 2/13/24
    # This code will prompt the user for a radius in a funciton, then calculate and print out the circumference of the circle using 
        # another function, which can be called from another script. 
    #Formula info:
        #https://www.cuemath.com/geometry/circumference-of-a-circle/
    #Author: CUEMATH, no date created, accessed 1/31/24
   print()
   radius = float(input("Please enter the radius of your circle: ")) #input of radius
   answer = circleCircumference(radius)
   return answer

if __name__ == "__main__":
    main()