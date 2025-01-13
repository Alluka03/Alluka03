# to create a simple choosing game using multiple functions

from random import shuffle

Ball_list = [" ", "O", " "]

def shuffled_list(my_list):
          shuffle(my_list)
          return my_list

def player_guess():
          guess = ''
          while guess not in ["0","1","2"]:
                    guess = input("Pick a choice from 0, 1, 2: ") 
          return int(guess)               

def check_guess(my_list,guess):
          if my_list[guess]=="O":
                    print("Correct! You won.")
          else:
                    print("Lost! Please try again")
                    
print(check_guess(shuffled_list(Ball_list),player_guess()))

"""
In this program: 
1. We first import the shuffle function from the random module.
2. Defined the Ball list.
3. Function for shuffling a list.
4. Function for getting the player's guess.
5. Function for checking the player's guess.
6. We call the functions in order as (check guess) as it has main part of the program inside which 
we call shuffled_list()function and player_guess()function

"""