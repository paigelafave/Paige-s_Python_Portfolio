#function: calculateResistance
def calculateResistance(current, voltage):
    resistance = voltage / current
    str_resis= str(resistance) #convert resistance to string
    print("The average score of the resistance is " + str_resis) # print voltage
    print()
    return str_resis


#input and print answer function as main
def main():
    # Lab Week 5
    #calculateVoltage.py
    #By: Paige LaFave
    # Created 2/13/24
    #This code will prompt the user for the current and resistance in a function, then calculate the voltage in another function, 
        # which can be called from another script. 
    #Formula info:
        #https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law
    # Author: Fluke, no date created, accessed 1/31/24
    print()
    current = float(input("Please enter the current: " )) #input of current
    print()
    voltage = float(input("Please enter the voltage: ")) #input of voltage
    print()
    answer = calculateResistance(current, voltage)
    return answer

if __name__ == "__main__":
    main()