#Joey Clayton Jr 
# LAB 1
# 1-6-2026

# You will be writing one Python file for this project - it is a program that determines whether a
# meeting room is in violation of fire regulations regarding the maximum room capacity. The
# program will accept the maximum room capacity and the number of people attending the
# meeting. If the number of people is less than or equal to the maximum room capacity, the
# program announces that it is legal to hold the meeting and tells how many additional people may
# legally attend. If the number of people exceeds the maximum room capacity, the program
# announces that the meeting cannot be held as planned due to the fire regulation and tells how
# many people must be excluded in order to meet the fire regulations. The user should be allowed
# to enter and check as many rooms as they would like without exiting the program.

#---FUNCTIONS----------------------------------------------------------
#function definition below - must define before calling in main code (using)
def difference(people,max_cap):
    diff = max_cap - people

    #the return value replaces the function call
    return diff #when diff < 0, too many people for a room 
def decision (a):
     #error trap loops!
    while a != "y" and a != "n":
        print("***Invalid Entry - 'y' or 'n' only!")
        a = input("\t\tWould you like to see another room? [y/n]: ").lower()
    
    return a 

#---MAIN CODE----------------------------------------------------------

#function call below - actually the function
print(f"The difference is : {difference(22, 25)}") 

print("\n\t\tWelcome To My Home\n")

answer = "y"

while answer == "y" :
    name = input("\nEnter The Name Of The Room: ")
    cap = int(input(f"Enter The Max Capacity for {name} room: "))
    attending = int(input(f"Enter The Number Of People Attending The Meeting In {name} Room: "))


    diff_return = difference(attending, cap)
    
    if diff_return >= 0 :
        print(f"Room meets fire safety code. You can add {diff_return} people")   
    else:
        print(f"Room Doesnt meet fire safety code. You must remove {diff_return * -1} people")
    answer = input("\t\tWould you like to see another room? [y/n]: ").lower()

    answer = decision(answer)

print(f"GoodBye From The Stark Family")