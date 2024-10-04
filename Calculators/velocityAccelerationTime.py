#function: velocityAccelerationTime
def velocityAccelerationTime(v0, acceleration, time):
    print()
    final_velocity = v0 + (acceleration * time)
    final_velocity = str(final_velocity) #convert distance to string
    print("The final velocity is " + final_velocity + " m/s.") # print distance
    return final_velocity


#input and print answer function as main
def main():
    # Lab Week 5
    #velocityAccelerationTime.py
    #By: Paige LaFave
    # Created 2/13/24
    #This code will prompt a user for an initial velocity, acceleration, and time using a function. Then calculate print the final 
        # velocity using another funciton, which can be called from a different script. 
    #Formula info:
        #https://www.geeksforgeeks.org/velocity/
    # Author: Geeksforgeeks, no date created, accessed 1/31/24
    print()
    v0 = float(input("Please enter your initial velocity in meters per second: ")) #input of v0
    print()
    acceleration = float(input("Please enter the acceleration in meters per second squared: "))#input of acceleration
    print()
    time = float(input("Please enter the time in seconds: ")) #input of time
    print()
    answer = velocityAccelerationTime(v0, acceleration, time)
    return answer

if __name__ == "__main__":
    main()