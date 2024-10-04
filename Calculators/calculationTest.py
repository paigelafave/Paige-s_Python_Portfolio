#Lab Week 5
# 2/13/24
# By: Paige LaFave

#This script will allow the user to use 1 of 4 calculators: Shapes (area and perimeter of rectangle and circle), Physics (velocity and distance),
    # Ohms Law (current, voltage, and resistance), and Useful Life Calculations (BMI and compound amount). You also have the option to quit.
    # Depending on which option you choose, you will be prompted for specific values to determine the desired calculation. The calculation will
    # be printed and the program will continue to run until you "quit". 


import myShapes
import myPhysics
import myOhmsLaw
import myUsefulLifeCalcs

y = True
def main():
    global y
    while y == True:
        y = True
        print()
        y = input("Would you like to use [s]hapes, [p]hysics, [o]hms law, [u]seful life calculations, or [q]uit? ")


        if y == "s":

            z = input ("Would you like to calculate: [rp] rectangle perimeter, [ra] rectangle area, [c] circumference, or [ca] circle area? ")
            print()

            if z == "rp":
                print()
                base = float(input("Please enter the base length of your rectangle: ")) #input of base
                print()
                height = float(input("Please enter the height of your rectangle: ")) #input of height
                print()
                myShapes.rectanglePerimeter(base, height)
                y = True


            elif z == "ra":
                print()
                base = float(input("Please enter the base length of your rectangle: ")) #input of base
                print()
                height = float(input("Please enter the height of your rectangle: ")) #input of height
                print()
                myShapes.areaOfRectangle(base, height)
                y = True

            elif z == "c":
                print()
                radius = float(input("Please enter the radius of your circle: ")) #input of radius
                print()
                myShapes.circleCircumference(radius)
                y = True

            elif z == "ca":
                print()
                radius = float(input("Please enter the radius of your circle: "))#input of radius
                print()
                myShapes.areaOfCircle(radius)
                y = True

            else: 
                print()
                print()
                print("Error, please enter [ra], [rp], [c], or [ca] (case sensitive).")
                print()
                y = True



        elif y == "p":
            z = input("Would you like to calculate [d]istance or [v]elocity? ")
            print()

            if z == "d":
                print()
                speed = float(input("Please enter speed in meters per second: ")) #input of speed
                print()
                time = float(input("Please enter the time in seconds: ")) #input of time
                print()
                myPhysics.distanceSpeedTime(speed, time)
                y = True


            elif z == "v":
                print()
                v0 = float(input("Please enter your initial velocity in meters per second: ")) #input of v0
                print()
                acceleration = float(input("Please enter the acceleration in meters per second squared: "))#input of acceleration
                print()
                time = float(input("Please enter the time in seconds: ")) #input of time
                print()
                myPhysics.velocityAccelerationTime(v0, acceleration, time)
                y = True

            else:
                print()
                print()
                print("Error, please enter [d] or [v] (case sensitive).")
                print()
                y = True


        elif y == "o":
            z = input("Would you like to calculate [r]esistance, [v]oltage, or [c]urrent? ")
            print()

            if z == "r":
                print()
                current = float(input("Please enter the current: " )) #input of current
                print()
                voltage = float(input("Please enter the voltage: ")) #input of voltage
                print()
                myOhmsLaw.calculateResistance(current, voltage)
                y = True


            elif z == "v":
                print()
                current = float(input("Please enter the current: " )) #input of current
                print()
                resistance = float(input("Please enter the resistance: ")) #input of resistance
                print()
                myOhmsLaw.calculateVoltage(current, resistance)
                y = True


            elif z == "c":
                print()
                voltage = float(input("Please enter the voltage: " ))#input of voltage
                print()
                resistance = float(input("Please enter the resistance: ")) #input of resistance
                print()
                myOhmsLaw.calculateCurrent(voltage, resistance)
                y = True


            else:
                print()
                print()
                print("Error, please enter [r], [v], or [c] (case sensitive).")
                print()
                y = True



        elif y == "u":
            z = input("Would you like to calculate [b]mi or [c]ompound amount? ")
            print()

            if z == "b": 
                print()
                weight = float(input("Please enter your weight in pounds: " )) #input of weight
                print()
                height = float(input("Please enter your height in inches: ")) #input of height
                print()
                myUsefulLifeCalcs.bodyMassIndex(weight, height)
                y = True


            elif z == "c":
                print()
                principal = float(input("Please enter the principle amount: ")) #input principle
                print()
                rate = float(input("Please input the interest rate in percentage (do not enter %): ")) #input interest rateprint()
                number_compounds = float(input("Please enter the number of times the interest compounds each year: "))#input compound amount
                print()
                time = float(input("Please enter the time in years: ")) #input time in years
                print()
                myUsefulLifeCalcs.compoundAmount(principal, rate, number_compounds, time)
                y = True


            else:
                print()
                print()
                print("Error, please enter [u] or [c].")
                y = True



        elif y == "q":
            y = False
            print()
            print("Goodbye!")
            print()



        else:
            print()
            print()
            print("Error, please enter [s], [p], [o], [u], or [q] (case sensitive).")
            print()
            y = True


if __name__ == "__main__":
    main()








            
                     
                     
                     
                     
            
