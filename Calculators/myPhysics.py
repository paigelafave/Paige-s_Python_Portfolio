#Lab Week 5
# 2/13/24
# By: Paige LaFave
# This is a module containing the functions calculating distance and velocity.
    # Called in the file "calculationTest.py".


#function: distanceSpeedTime
def distanceSpeedTime(speed, time):
    distance = speed * time # distance formula
    str_dist = str(distance) #convert distance to string
    print()
    print()
    print("The distance traveled is " + str_dist + " m/s.") # print distance
    print()
    return str_dist

#function: velocityAccelerationTime
def velocityAccelerationTime(v0, acceleration, time):
    print()
    final_velocity = v0 + (acceleration * time)
    final_velocity = str(final_velocity) #convert distance to string
    print()
    print()
    print("The final velocity is " + final_velocity + " m/s.") # print distance
    print()
    return final_velocity