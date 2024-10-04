#function: distanceSpeedTime
def distanceSpeedTime(speed, time):
    distance = speed * time # distance formula
    str_dist = str(distance) #convert distance to string
    print("The distance traveled is " + str_dist + " m/s.") # print distance
    print()
    return str_dist


#input and print answer function as main
def main():
    # Lab Week 5
    #distanceSpeedTime.py
    #By: Paige LaFave
    # Created 2/13/24
    # This code will prompt a user for the speed and time in a function. Then calculate and print the distance using anthoner function,
        # which can be called from another script. 
    #Formula info:
        #https://www.purplemath.com/modules/distform.htm
    # Author: Purple Math, no date created, accessed 1/31/24
    print()
    speed = float(input("Please enter speed in meters per second: ")) #input of speed
    print()
    time = float(input("Please enter the time in seconds: ")) #input of time
    print()
    answer = distanceSpeedTime(speed, time)
    return answer

if __name__ == "__main__":
    main()