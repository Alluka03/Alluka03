#mystring = range(0,10)
"""mylist = [letter for letter in range(0,10) if letter%2 == 0 ]
print(mylist)"""

"""for star in mystring:
          mylist.append(star)
          myfinal_list = mylist
print(myfinal_list)"""

"""speed = [10,20,40,50,60,1,2.5]
mylist = [x**2 for x in speed if x%2==0 ]
print(mylist)"""

a = range(0,10)
mylist = [x if x%2 == 0 else "ODD" for x in a]
print(mylist)