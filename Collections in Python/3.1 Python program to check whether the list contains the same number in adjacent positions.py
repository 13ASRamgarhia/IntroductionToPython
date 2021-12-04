'''
Given a list of integer values, write a Python program to check whether the list contains the same number in adjacent positions.
Display the count of such adjacent occurrences.

=============================================
Sample List                     Sample Output
---------------------------------------------
[1,1,5,100,-20,-20,6,0,0]       3
[10,20,30,40,30,20]             0
[1,2,2,3,4,4,4,10]              3
=============================================
'''

sample_list1 = [1,1,5,100,-20,-20,6,0,0]
sample_list2 = [10,20,30,40,30,20]
sample_list3 = [1,2,2,3,4,4,4,10]

print("*"*48)
print("*  Sample List 01 : [1,1,5,100,-20,-20,6,0,0]  *")
print("*  Sample List 02 : [10,20,30,40,30,20]        *")
print("*  Sample List 03 : [1,2,2,3,4,4,4,10]         *")
print("*"*48)

try:
    i = int(input("\nEnter 1,2,3 to select sample list 1,2,3 respectively -> "))
    counter = 0
    print("-"*58)

    if(i == 1):
        for index in range(len(sample_list1)-1):
                if(sample_list1[index] == sample_list1[index+1]):
                    counter += 1

        print(f"{counter} adjacent occurances")

    elif(i == 2):
        for index in range(len(sample_list2)-1):
            if(sample_list2[index] == sample_list2[index+1]):
                counter += 1

        print(f"{counter} adjacent occurances")

    elif(i == 3):
        for index in range(len(sample_list3)-1):
            if(sample_list3[index] == sample_list3[index+1]):
                counter += 1

        print(f"{counter} adjucent ccurances")

    else:
        print("Please select an option as 1, 2, or 3 only")

except ValueError:
    print("-"*58)
    print("Please select an option as 1, 2, or 3 only")