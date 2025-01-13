# to check if the number is even
"""def even_function(divid = input(),divs = 2):
          if int(divid)%divs==0:
                    return True
          else:
                    return False

print(even_function())"""

"""#short form of the above program
def even_function(number):
          return number%2==0
print(even_function(20))"""

#to check if the number is even inside a list and append the even numbers accordingly
def even_list_function(num_list):
          even_list = [number for number in num_list if number %2 == 0]
          return even_list
print(even_list_function([1,2,3,4,5,6]))


          
