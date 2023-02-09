def TestTask1_Ver1():
    print('Please enter the number bigger then 7 for say "Hello"')
    num = float(input())
    if num > 7:
        print('Привет')

def TestTask1_Ver2():
    print('Please enter the number bigger then 7 for say "Hello". For exit enter the number less 7')
    num = float(input())
    while num > 7:
        print('Привет')
        num = float(input())

# Menu: you may choose version for operation between simple mode and endless mode (ended when num < 7)
print('Please choose Version for operation. Enter 1 (simple mode) or 2 (endless mode)')
choose_VersionTask1 = int(input())
if choose_VersionTask1 == 1:
    TestTask1_Ver1()
elif choose_VersionTask1 == 2:
    TestTask1_Ver2()
else:
    print('Incorrect number of Version. Please enter 1 or 2')