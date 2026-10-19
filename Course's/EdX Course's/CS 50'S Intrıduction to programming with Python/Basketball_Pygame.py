#Get imputs from user
user_input = int(input("Enter a score(0 to exit): "))

#Make Dictionary
Scores = []


#While loop for working
While True:
    if user_input == 0:
        print("Scores:", Scores)
        break
    
    elif user_input == 1:
        Scores.append(1)
        print("Scores:", Scores)
        
    elif user_input == 2:
        Scores.append(2)
        print("Scores:", Scores)
        
    elif user_input == 3:
        Scores.append(3)
        print("Scores:", Scores)
    
    else:
        print("Error: Invalid score. Please enter a score between 1 and 3, or 0 to exit.")
        print("Scores:", Scores)
        continue
