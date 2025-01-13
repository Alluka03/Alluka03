#test program #
userid = input("Please input the userid: ")
sys_userid = "Alluka03"

if userid == sys_userid:
          print("Correct ID \n Verification 1 successful. ")
else :
          print("Incorrect ID \n Verificaton 1 unsuccessful. ")

password = input("Please input the password: ")
sys_password = "Sahil@123"

if password == sys_password:
          print("Correct Password \n Verification 2 successful. ")
else:  
          print("Incorrect Password \n Verification 2 unsuccessful. ")
          
if userid == sys_userid and password == sys_password:
          print("Access Granted \n Welcome to the system. ")
else:
          print("Access Denied \n Please try again. ")