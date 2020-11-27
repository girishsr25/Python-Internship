#Day 5 Task

#1

def calc():

    
    x = int(input("Enter first number: "))               # x = 10
    y = int(input("Enter second number: "))              # y = 5
    print("Adding of two numbers is "+ str(x+y))         #output = 15
    print("Subtraction of two numbers is "+ str(x-y))    #output = 5
    print("Division of two numbers is "+ str(x//y))      #output = 2
    print("Multiplication of two numbers is "+ str(x*y)) #output = 50

calc()

#2

def covid(name,temp=98):
    print("Patient name is " + name + " and his body temperature is " + str(temp))

covid("Akhil")

#output = Patient name is Akhil and his body temperature is 98


