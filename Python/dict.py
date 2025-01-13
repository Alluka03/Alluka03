#dict = {} \\ID PASSWORD Dictionary Test
#id = input("Enter the ID: ")
#password = input("Enter the desired password: ")
#dict[id] = password
#print(dict)
""""
my_dict = {"Apple" :{260:"5 apples"}, "Banana" : 60, "Chikoo" : 150, "Dragon Fruit" : {280 : "consists of only 2 fruits mostly in a kg"}} #defining dict
print("The available fruits and prices are: ", (list(my_dict))) #printing all the fruits as keys for customer

key = input("Enter which fruit you want: ") #input from customer regarding the fruit needed

if key in my_dict: #deifining if else loop to check if the key/fruit is present in the dict
          value = my_dict[key] #checking the value for the key
          print("The prices for" , key, "are" ,value ,"per kg") # to print if the key the is found
else:
          print("The above input selected is not available in store. \n Please do visit later. \n Thank you") # to print is key is not found          

a = my_dict["Apple"]     
print("The price of apple is: ",a)
b = my_dict["Apple"][260]
print("Number of apples in 1 kilo are approx: ",b)"""


"""
a = {"key1" : ["a", "b", "c", "d"], "key2" : ["e", "f", "g", "h"]}
list = a["key1"][2].upper()
list_2 = a["key2"][3].upper() 
#print(list + list_2)
a["key3"] = ["i","j","k","l"]
#print("The new list is " ,a)
list_3 = a["key3"][0].upper()
list_4 = a["key1"][2].upper()
list_5 = a["key3"][2].upper()
final_list = list+list_2+list_3+list_4+list_5 
print("The final word is :", list+list_2+list_3+list_4+list_5)
print(a.items())
"""
car = {
          "model" : "Ford Mustang",
          "DOM" : "23.1.1979",
          "color" : "core black"
}
print("The model of the car is",car["model"])


