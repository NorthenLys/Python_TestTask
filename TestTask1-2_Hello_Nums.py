print('There is random test tasks based on simple operations. Please follow the instructions.')
def num_bigger_then_7():
    print('Please enter the number bigger then 7 for say "Hello"')
    num = float(input())
    if num > 7:
       return print('Have a nice day, people!')
    else:
        return print('This number lower then 7. Please try again.')
def hello_name():
    print('Please enter your name')
    name = str(input())
    if name == 'Алиса' or name == 'Alice' or name == 'Alisa':
        return print('Glory to you master,', name,'!')
    else:
        return print('Name does not exist a person named', name)
# Menu: you can choose the operation between enter the num and enter the name
def menu():
    print('Choose an operation. Enter 1 (enter the num) or 2 (enter the name)')
    choose_operation = int(input())
    if choose_operation == 1:
        return num_bigger_then_7()
    elif choose_operation == 2:
        return hello_name()
    else:
        return print('Incorrect the number of the operation. Please enter 1 or 2')
menu()
