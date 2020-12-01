#Day 9
#1
def mul(x):
    return lambda y : x * y

val = mul(4)
print(val(3))

#output = 12

#2
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], 
                                 range(n-2), [0, 1]) 
  
print(fib(5))

#output = [0, 1, 1, 2, 3]

#3
nums = [1,2,3,4,5]
n = 2
new_list = list(map(lambda x: x*n,nums))
print(new_list)

#output = [2, 4, 6, 8, 10]

#4
nums = [3,9,12,87,90]
n = 9
new = list(filter(lambda x: (x%9==0),nums))
print(new)

#output = [9, 90]

#5
even = [2,9,10,7,8]
count = list(filter(lambda x: (x%2==0),even))
print(len(count))

#output = 3
