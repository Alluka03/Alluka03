work_hours = [("Sahil",900),("Shaun",600),("Umesh",100),("Yash",500)]
def employee_of_the_month(work_hours):
          current_max_hours = 0
          employee_month = ''
          for employee,hours in work_hours:
                    if hours > current_max_hours:
                              current_max_hours = hours
                              employee_month = employee
                    else:
                              pass
          return(employee_month, current_max_hours)
print(employee_of_the_month(work_hours))
#direct tuple unpacking while calling the function
name,hours = employee_of_the_month(work_hours)
print(name)
print(hours)