
"""
A program to calculate volume for a specified solid using a menu system
"""
import math


# priming read, display menu & get user's initial choice
print("*****************************************")
print("*Calculation of Volume for Solid Objects*")
print("*****************************************")
print(" 1.\t Cube                ")
print(" 2.\t Cylinder        ")
print(" 3.\t Sphere       ")
print(" 4.\t Exit          ")
print(" **********************************")
user_choice = int(input("Option:"))

# loop until exit option chosen
while user_choice != 4:
    if user_choice == 1:
        # Enter length of the cube for calculation
        length = float(input("Enter the length of the cube:  "))
        # calculate volume
        volume = length ** 3
        #  print out the volume
        print("The volume for this cube is:  ", volume)
        print()
    elif user_choice == 2:
        # Enter radius and height of the cylinder for calculation
        radius = float(input("Enter the radius of the cylinder:  "))
        while radius <= 0:
            radius = float(input("Re-enter the radius of the cylinder:  Error in value"))

        height = float(input("Enter the height of the cylinder:  "))
        # calculate volume
        volume = math.pi * (radius ** 2) * height
        # print out the  volume
        print("The volume for this cylinder is: ", round(volume, 2))
        print()
    elif user_choice == 3:
        # Enter radius of the sphere for calculation
        radius = float(input("Enter the radius of the sphere:  "))
        while radius <= 0:
            radius = float(input("Re-enter the radius of the cylinder:  Error in value"))
        # calculate volume
        volume = (4 / 3.0) * math.pi * (radius ** 3)
        # print out the volume
        print("The volume for this sphere is: ", round(volume,2))
        print()
    else:
        print("Invalid menu option chosen")
    # display menu and get user 's next option in order to make progress in loop
    print("*****************************************")
    print("*Calculation of Volume for Solid Objects*")
    print("*****************************************")
    print(" 1.\t Cube                ")
    print(" 2.\t Cylinder        ")
    print(" 3.\t Sphere       ")
    print(" 4.\t Exit          ")
    print(" **********************************")
    user_choice = int(input("Option:"))
# end of menu
print("Processing of Volumes completed")