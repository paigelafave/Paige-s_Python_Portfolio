#funciton: calculateCurrent
def calculateCurrent(voltage, resistance):
    current =  voltage / resistance
    str_curr = str(current) #convert current to string
    print("The average score of the current is " + str_curr) # print current
    print()
    return str_curr


#input and print answer function as main
def main():
    # Lab Week 5
    #calculateCurrent.py
    #By: Paige LaFave
    # Created 2/13/24
    #This code will prompt the user for voltage and resistance in a function, then calculate and print the current using another function,
        # which can be called by a different script. 
    #Formula info:
        #https://byjus.com/physics/ohms-law/
    # Author: BYJU's, no date created, accessed 1/31/24
    print()
    voltage = float(input("Please enter the voltage: " ))#input of voltage
    print()
    resistance = float(input("Please enter the resistance: ")) #input of resistance
    print()
    answer = calculateCurrent(voltage, resistance)
    return answer

if __name__ == "__main__":
    main()