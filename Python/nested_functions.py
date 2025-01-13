#LEGB RULE:
""" 
L : Local : Searching of variables locally (basically defined in a function or lambda)
E : Enclosed Function : Searching of variable in enclosed function(function or lambda)
G : Global : Searching of variables globally when they are not found in L & E respectively(defined outside the function)
B : Built-in : 
"""


x = 50 
def global_check():
          print("GLOBAL",x)
          def enclosed_check():
                    x = 100
                    print("ENCLOSED",x)
                    def local_check():
                              x = 200
                              print("LOCAL",x)
                    print(local_check())
          print(enclosed_check())
print(global_check())