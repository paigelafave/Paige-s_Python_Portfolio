#function: compoundAmount
def compoundAmount(principal, rate, number_compounds, time):
    accrued_amount = principal * (1 + (rate/100) / number_compounds) **(number_compounds * time) #compound interest formula
    accrued_amount = str(accrued_amount) #convert accrued amount to string
    print("The amount of compound interest is " + accrued_amount) #print
    print()
    return accrued_amount


#input and print answer function as main
def main():
    # Lab Week 5
    #compound.py
    #By: Paige LaFave
    # Created 2/13/24
    #This code will prompt the user for the principle amount, interest rate, and the number of time the interest compouds in year in
        # a function. Then calculate and print our the coumpound amount in another function, which can be called from another script. 
    #Formula info:
        #https://www.geeksforgeeks.org/compound-interest-formula/
    # Author: geeksforgeeks, no date created, accessed 1/31/24
    print()
    principal = float(input("Please enter the principle amount: ")) #input principle
    print()
    rate = float(input("Please input the interest rate in percentage (do not enter %): ")) #input interest rate
    print()
    number_compounds = float(input("Please enter the number of times the interest compounds each year: "))#input compound amount
    print()
    time = float(input("Please enter the time in years: ")) #input time in years
    print()
    answer = compoundAmount(principal, rate, number_compounds, time)
    return answer

if __name__ == "__main__":
    main()