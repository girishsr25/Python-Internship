#Day 11 Task

#1
x = [1,2,3]
y = [4,5,6]
z = list(zip(x,y))
print(z)

#output = [(1, 4), (2, 5), (3, 6)]

#2

rang = range(1,9)
lst = [2,4,6,8,10,12,14,16]
merge = zip(rang,lst)
print(list(merge))

#output = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16)]

#3

lst = [4,78,45,12,54]
lst.sort()
print("Ascending Order: ")
print(lst)

#output = Ascending Order: 
        #[4, 12, 45, 54, 78]

#4

def fil(nums):
    if nums%2==0:
        return True
    else:
        return False
inp = [1,8,9,4,78,7,10,9]
filtered = filter(fil,inp)
print("The filtered numbers are: ")
for i in filtered:
    print(i)

#output = The filtered numbers are: 
            #8
            #4
            #78
            #10

