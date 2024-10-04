#Lab Week 5
# 2/13/24
# By: Paige LaFave
# This is a module containing the functions calculating body mass index and compound amount. 
    # Called in the file "calculationTest.py".

# function: bodyMassIndex
def bodyMassIndex (weight, height):
    BMI = (weight / (height ** 2)) * 703
    str_BMI = str(BMI) #convert bmi to string
    print()
    print()
    print("Your body mass index is " + str_BMI) # print bmi
    print()
    return str_BMI

#function: compoundAmount
def compoundAmount(principal, rate, number_compounds, time):
    accrued_amount = principal * (1 + (rate/100) / number_compounds) **(number_compounds * time) #compound interest formula
    accrued_amount = str(accrued_amount) #convert accrued amount to string
    print()
    print()
    print("The amount of compound interest is " + accrued_amount) #print
    print()
    return accrued_amount