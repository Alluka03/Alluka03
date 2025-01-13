def user_choice():
    
    choice = "CHOICE"
    acceptable_range = range(0, 10)
    within_range = False
    
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input("Enter a number in the range : ")
        
        if choice.isdigit()==False:
            print("Enter a digit")
        
        if choice.isdigit()==True:
            
            int_choice = int(choice)
           
            if int_choice in acceptable_range:
                within_range = True
            else:
                print("Input a number within the range (0 - 10)")
                within_range = False
                
    return(int_choice)

print(user_choice())