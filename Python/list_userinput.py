my_list = []

a = int(input("The number of elements to be given in list: ")) # number of elements to be present in the list

for i in range(0,a): #for loop for iterating over every element to list
          ele = str(input()) # input for each element in list
          my_list.append(ele)# appending all the elements in the list

print("This is the restaruants menu" ,my_list) # to present the final list 

name = input("what do you want: ")

if name in my_list:
          print("Item is present in the menu : ", name)
else:
          print("Item is not present in the menu. Please try again ", name)