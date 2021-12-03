'''
An organization has decided to provide salary hike to its employees based on their job level.
Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:

============================================================
Job level     Hike Percentage (applicable on current salary)
------------------------------------------------------------
3             15
4             7
5             5
============================================================
In case of invalid job level, consider hike percentage to be 0.
Given the current salary and job level, write a Python program to find and display the new salary of an employee.
'''

try:
    curr_salary = int(input("Enter your salary : "))
    job_lvl = int(input("Enter job level   : "))

    if(job_lvl == 3):
        new_salary = curr_salary + (0.15*curr_salary)

    elif(job_lvl == 4):
        new_salary = curr_salary + (0.07*curr_salary)

    elif(job_lvl == 5):
        new_salary = curr_salary + (0.05*curr_salary)

    else:
        new_salary = curr_salary

    print("-"*35)
    print(f"Your new salary is {new_salary}")

except ValueError:
    print("-" * 35)
    print("Please enter in numbers only")