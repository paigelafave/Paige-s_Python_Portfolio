#function: calculateVoltage
def calculateVoltage(current, resistance):
    voltage = current * resistance
    str_vol = str(voltage) #convert voltage to string
    print("The average score of the voltage is " + str_vol) # print voltage
    print()
    return str_vol


#input and print answer function as main
def main():
    # Lab Week 5
    #calculateVoltage.py
    #By: Paige LaFave
    # Created 2/13/24
    #This code will prompt the user for the current and resistance in a function, then calculate the voltage using another function
        #  which can be used inside another script. 
    #Formula info:
        #https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law
    # Author: Fluke, no date created, accessed 1/31/24
    print()
    current = float(input("Please enter the current: " )) #input of current
    print()
    resistance = float(input("Please enter the resistance: ")) #input of resistance
    print()
    answer = calculateVoltage(current, resistance)
    return answer

if __name__ == "__main__":
    main()