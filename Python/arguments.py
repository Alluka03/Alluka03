"""def myfunction(*args):
          return sum((args))*0.05

print(int(myfunction(10,20,30)))"""

"""def my_func(**kwargs):
          if "fruits" in kwargs:
                    print ("My favourite fruit is: ",kwargs["fruits"])
          else:
                   print("No fruit") 
                    
print(str(my_func(fruits = 'apple')))"""

def my_func(*args,**kwargs):
          print ("I would like to have",args[0],kwargs['food'],args[1],kwargs["animal"], args[2], kwargs["tree"],"as I want to start a big farm")
print(my_func(10,20,30,tree = 'Mangoes', animal = 'Horses', food = 'Chickens'))
          