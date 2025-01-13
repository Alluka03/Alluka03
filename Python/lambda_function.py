#to reduce the iteration of loops using map and filter function:

#map function
#This function works same as for loop
nums_list = [1,2,3,4,5,6,7]
names_list = ["Sahil","Gauri","Baby"] # to find which string is even and which is odd
"""
def square_function(nums):
          return nums**2

for items in map(square_function,nums_list):
          pass
          
print(list(map(square_function,nums_list)))"""


"""def names_even(my_list):
                    if len(my_list)%2==0:
                              return "EVEN"
                    else:
                              return ("ODD",my_list)

print(list(map(names_even,names_list)))"""

# filter function: 
#This function is used to filter the given values as per the defined condition:

"""my_list = [1,2,3,4,5,6]
def filter_function(nums):
          return nums % 2 == 0

print(list(filter(filter_function,nums_list)))"""

# lambda function:
#lambda function is used to simplify the program by removing the def keyword and return keyword and placing the whole program directly in one line
#lambda function is used to create small anonymous functions.
#lambda num : num%2==0
#we can use both filter function and map function to create one line small functions.
"""print(list(map(lambda num : num**2,nums_list)))
print(list(filter(lambda num : num**2,nums_list)))"""

print(list(map(lambda x : x[0],names_list)))
print(list(filter(lambda y : len(y)%2==0,names_list)))