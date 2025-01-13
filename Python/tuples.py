#Tuples are immutable i.e. they can be changed as list and dict. do

t = ("a", "b", "c", "c","b", "a","c")
print(t)
print(type(t))
print(t[2])
print("Number of times a occurs",t.count("a"), "Number of times b occurs", t.count("b"), "Number of times c occurs",t.count("c"))
print(t.index("c"))
