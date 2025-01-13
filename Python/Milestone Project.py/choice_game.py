# USER CHOICE FOR FIRST MILESTONE PROJECT * * * 


basic_list = [0, 1, 2]
acceptable_values = ['0', '1', '2']
acceptable_start_input = ['Y', 'N']
game_on = True

def display_row(basic_list):
    print("Here is the starting row:", basic_list)

def position_choice():
    choice = "BASIC_WRONG"
    while choice not in acceptable_values:
        choice = input("Enter a position choice from (0 - 2): ")
        if choice not in acceptable_values:
            print("Invalid choice, please try again.")
    return int(choice)

def replacement_choice(basic_list, position):
    string_input = input("Enter a string to replace at the position: ")
    basic_list[position] = string_input
    print("Your updated list is:", basic_list)

def user_start_choice():
    user_choice = "BASIC_WRONG"
    while user_choice not in acceptable_start_input:
        user_choice = input("Want to play more ('Y' or 'N')? ")
        if user_choice not in acceptable_start_input:
            print("Please enter a valid input.")
    if user_choice == 'Y':
        return True
    else:
        return False

while game_on:
    display_row(basic_list)
    position = position_choice()
    replacement_choice(basic_list, position)
    game_on = user_start_choice()
