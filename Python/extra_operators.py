"""
for x in range(0,6):
          print(x)
"""

"""a = list(range(0,10,4))
print (a)"""

"""index_count = 0
for x in "Sahil Zanzane" :
          print("At index",index_count,"the letter is",x)
          index_count += 1"""
          
"""#word = "Sahil"
for index,values in enumerate("Sahil"):
          print(index)
          print(values)
          print("\n")"""
          
list1 = [1,2,3,4]
list2 = ["a","b","c","d"]
list3 = ["e","f","g","h"]
"""for num,letr,l1 in zip(list1,list2,list3):
          print(num)
          print(letr)
          print(l1)
print(list(zip(list1,range(1,5),list2,list3)))
      """    


"""a = {"mykey" : 345}
print("mykey" in a)
print(345 in a.values())"""

"""a = ["10","30","40", "100", "1"]
print(min(a))
print(max(a))"""

"""from random import shuffle
a = [10,20,30,40,50,60,1,2,100]
shuffle(a)
print(a)
print("The min from shuffled list",min(a))
print("The max from shuffled list",max(a))"""

from random import randint
b = input("Enter the lucky number: ")
a = randint(0,100)
if a == b :
          print("You won the lottery")
else:
          print("The lottery number is",a,"Please try again later.\n Thank you")