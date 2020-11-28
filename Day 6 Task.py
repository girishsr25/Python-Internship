#Day 6 Task

#Task 1

my_list = [2,3,5,8,10]
new_list = []
for i in my_list:
    new_list.append(i+2)
print(new_list)


#Task 2
print("Pattern")
def num(n):
    if n==0:
        return
    else:
        for i in range(n,0,-1):
            print(i,end="")
    print()
    num(n-1)

num(5)


#Task 3

def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
print("Fibonacci series")
val = int(input("Enter number to generate fibonacci series"))
fib(val)

#Task 4

"""
Armstrong number : If the sum of cubes of individual digits is equal to the
                given number itself then the number is "Armstrong number"
"""

def check_armstrong(num):
    n=0
    temp = num
    if num==0:
        return
    else:
        while num > 0:
            r = num%10
            num = num//10
            n = n+(r*r*r)
        if n == temp:
            print("It is an Armstrong number")
        else:
            print("It is not an Armstrong number")
inp = int(input("Enter number to check armstrong number or not: "))
check_armstrong(inp)

#Task 5

print("Multiplication tables of 9")
for i in range(1,11):
    print("9 x %d = %d" %(i,i*9))

#Task 6

n = int(input("Enter number to check positive or negative: "))
if n>=0:
    print("Positive number")
else:
    print("Negative number")


#Task 7

from math import *

ans = (sin(45) - cos(45)) * tan(30)
print(ans)

#Task 8

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter the choice: "))

if choice == 1:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result: ",a+b)
elif choice == 2:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result: ",a-b)
elif choice == 3:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result: ",a*b)
elif choice == 4:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result: ",a//b)
else:
    print("Please enter correct input")
    
