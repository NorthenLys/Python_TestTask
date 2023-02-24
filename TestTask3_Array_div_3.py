from numpy import random
def TestTask3_Version1():
    #Version 1 for manual input
    print('Please enter the numbers separated by a space. Ex: 0 1 3 -4 10 33')
    arr = [int(i) for i in input().split()]
    new_arr = []
    print(arr)
    for num in arr:
        if num%3==0:
            new_arr+=[num]
    print(new_arr)
    return new_arr
def TestTask3_Version2():
    #Version 2 for auto input
    print('Please wait. Program will do everything by random')
    random_arr = random.randint(100, size=(10))
    arr_div_3 = []
    print(random_arr)
    for num in random_arr:
        if num%3==0:
            arr_div_3+=[num]
    print(arr_div_3)
    return arr_div_3

# Menu: you can choose version for operation with arrays between manual and auto
print('Please choose the Version for an operation with an array. Enter 1 (manual) or 2 (auto)')
choose_Version = int(input())
if choose_Version == 1:
    TestTask3_Version1()
elif choose_Version == 2:
    TestTask3_Version2()
else:
    print('Incorrect a number of the Version. Please enter 1 or 2')
