#Day 8 Task

import os
line = lambda : print('-x-'*30)

#Task 1

#All types of errors in python
print(*dir(locals()['__builtins__']),sep = '\n')
# input('Press any key to clear')
line()

#Task 2

def user_input(datatype : type, number : int = 0, trigger : type = str):
    
    if number != 0:
        value = input(f'Enter the number {number}:')
        try:
            value = trigger(value)
        except:
            print('Invalid input')
            return user_input(datatype, number, trigger)
    else:
        value = input('Enter the operator :')
        if value not in '+-*%^&|/<>' or value.isalnum():
            try:
                raise Exception("Please Enter a valid operator")
            except Exception as e:
                print(e)
                return user_input(datatype, number)

    return str(value)




number1 = user_input(str, 1,float)
operator = user_input(str, 0, str)
number2 = user_input(str, 2,float)
try:
    print(eval(f'{number1}{operator}{number2}'))
except:
    print(eval(f'{int(float(number1))}{operator}{int(float(number2))}'))

line()
#Task 3

try:
    print(not_defined)
except NameError:
    print('Variable is not defined...')

line()

#Task 4

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:


#Task 5

while True:
    try:
        number = input("Enter a number..:")
        number = float(number)
        print('successful')
        break
    except:
        print('Invalid input')

line()
