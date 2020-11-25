#1

fruits = {1:"apple",2:"pineapple",3:"mango"}

vegetables = {4:"tomato",5:"potato",6:"onion"}

fruits.update(vegetables)

print(fruits)

#output = {1: 'apple', 2: 'pineapple', 3: 'mango', 4: 'tomato', 5: 'potato', 6: 'onion'}


#2

cars = {1:"BMW",2:"Benz",3:"Audi"}

cars.pop(3)

print(cars)

#output = {1: 'BMW', 2: 'Benz'}


#3

movies = ["The Irishmen", "Fight club", "John wick"]

directors = ["Martin Scorsese", "David Fincher", "Chad Stahelski"]

mapped_list = dict(zip(movies,directors))

print(mapped_list)

#output = {'The Irishmen': 'Martin Scorsese', 'Fight club': 'David Fincher', 'John wick': 'Chad Stahelski'}


#4

names = {"Girish", "Prakash", "Irfan", "Bill Gates"}

print(len(names))

#output = 4


#5

phones = {"Apple", "One plus", "Samsung", "Redmi"}

more_phones = {"Realme", "Samsung", "Oppo", "Vivo"}

phones.difference_update(more_phones)

print(phones)

#output = {'Apple', 'One plus', 'Redmi'}




