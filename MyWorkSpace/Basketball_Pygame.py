#Make Dictionary
Scores = {"Free Throws": 0, "Two Pointers": 0, "Three Pointers": 0}


#While loop for working
while (True):
    #Get imputs from user
    user_input = int(input("Enter a score(0 to exit): "))
    
    if user_input == 0:
        print("Scores:", Scores)
        break
    
    elif user_input == 1:
        Scores["Free Throws"] += 1
        print("Scores:", Scores)
        continue
        
    elif user_input == 2:
        Scores["Two Pointers"] += 1
        print("Scores:", Scores)
        continue
        
    elif user_input == 3:
        Scores["Three Pointers"] += 1
        print("Scores:", Scores)
        continue
    
    else:
        print("Error: Invalid score. Please enter a score between 1 and 3, or 0 to exit.")
        print("Scores:", Scores)
        continue

Total_Score = (Scores["Free Throws"] * 1) + (Scores["Two Pointers"] * 2) + (Scores["Three Pointers"] * 3)
print("Total Score:", Total_Score)