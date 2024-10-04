# function: bodyMassIndex
def bodyMassIndex (weight, height):
    BMI =  height / weight
    str_BMI = str(BMI) #convert bmi to string
    print()
    print("Your body mass index is " + str_BMI) # print bmi
    print()
    return str_BMI


#input and print answer function as main
def main():
    # Lab Week 5
    #bodyMassIndex.py
    #By: Paige LaFave
    # Created 2/13/24
    #This code will prompt the user for a weight and height in a function, then calculate and print the BMI using another function,
        # which can be called by another script. 
    #Formula info:
        #https://www.cdc.gov/healthyweight/assessing/bmi/index.html
    # Author: CDC, no date created, accessed 1/31/24
    print()
    weight = float(input("Please enter your weight: " )) #input of weight
    print()
    height = float(input("Please enter your height: ")) #input of height
    print()
    answer = bodyMassIndex(weight, height)
    return answer

if __name__ == "__main__":
    main()