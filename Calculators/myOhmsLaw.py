#Lab Week 5
# 2/13/24
# By: Paige LaFave
# This is a module containing the calculation functions of voltage, resistance, and current. 
    #Called in the file "calculationTest.py".


#function: calculateVoltage
def calculateVoltage(current, resistance):
    voltage = current * resistance
    str_vol = str(voltage) #convert voltage to string
    print()
    print()
    print("The average score of the voltage is " + str_vol) # print voltage
    print()
    return str_vol

#function: calculateResistance
def calculateResistance(current, voltage):
    resistance = voltage / current
    str_resis= str(resistance) #convert resistance to string
    print()
    print()
    print("The average score of the resistance is " + str_resis) # print voltage
    print()
    return str_resis

#funciton: calculateCurrent
def calculateCurrent(voltage, resistance):
    current =  voltage / resistance
    str_curr = str(current) #convert current to string
    print()
    print()
    print("The average score of the current is " + str_curr) # print current
    print()
    return str_curr

