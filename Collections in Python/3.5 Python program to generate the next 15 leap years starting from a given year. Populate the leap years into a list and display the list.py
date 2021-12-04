'''
Write a Python program to generate the next 15 leap years starting from a given year.
Populate the leap years into a list and display the list.
'''

try:
    year = int(input("Enter an year : "))
    if(year>0):
        def leap_years(year):
            leap_year_list = []
            print("-" * 91)
            for i in range(year,year+60):
                if(i%4 == 0):
                    leap_year_list.append(i)

            return leap_year_list

        print(leap_years(year))

    else:
        print("-"*91)
        print("Please enter a valid year")

except ValueError:
    print("-"*91)
    print("Please enter a valid year")