#Day 4 Task
#list exercise

my_list = [10,7,4,20,90]

#add an item
my_list.append(25)
print(my_list)      #output = [10, 7, 4, 20, 90, 25]

#delete
my_list.pop()          #deletes last element
print(my_list)      #output = [10, 7, 4, 20, 90]

#largest number
large = max(my_list)
print(large)         #output = 90

#smallest number
small = min(my_list)
print(small)         #output = 4

#tuple exercise

my_tuple = ("Girish",19,"Chennai","SEC")

#reverse tuple
print(my_tuple[::-1])      #output = ('SEC', 'Chennai', 19, 'Girish')

#convert tuple to list
new_list = []
new_list.extend(my_tuple)
print(new_list)            #output = ['Girish', 19, 'Chennai', 'SEC']


