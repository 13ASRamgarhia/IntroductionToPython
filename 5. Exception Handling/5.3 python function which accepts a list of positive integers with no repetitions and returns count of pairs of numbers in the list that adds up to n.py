'''
Write a python function, find_pairs_of_numbers(num_list,n) which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.

Example: num_list=[1, 2, 7, 4, 5, 6, 0, 3], n=6 output:3
         num_list=[3, 4, 1, 8, 5, 9, 0, 6], n=9 output:4
'''

num_list = [1, 2, 7, 4, 5, 6, 0, 3]
n = 6

def find_pairs_of_numbers(num_list,n):
    counter = 0

    for x in num_list:
        index = num_list.index(x)+1
        for y in range(index,len(num_list)):
            if(x + num_list[y] == n):
                counter = counter + 1

    return counter

print(num_list)
print(find_pairs_of_numbers(num_list,n))