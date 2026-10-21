#Take 2 number from user
Attemted = int(input("Enter the number of shots attempted: "))
Made = int(input("Enter the number of shots made: "))

#Control the user input
if Attemted < 0 or Made < 0:
    print("Error: The number of shots attempted and made cannot be negative.")
elif Made > Attemted:
    print("Error: The number of shots made cannot be greater than the number of shots attempted.")
elif Attemted == 0:
    print("Error: The number of shots attempted cannot be zero.")
else:
    #Calculate the percentage of shots made
    percentage = (Made / Attemted) * 100
    print(f"The shooting percentage is: {percentage:.1f}%")
