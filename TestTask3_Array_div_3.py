print('Please enter the numbers separated by a space. Ex: 0 1 3 -4 10 33')
arr = [int(i) for i in input().split()]
new_arr = []
for num in arr:
    if num % 3 == 0:
        new_arr += [num]
print(*new_arr)