from random import randint
# 'del spam[0]' deletes the thing at position 0
print("This proggram does this welcome to this program")

fruit = input("Give me a thing: ") #Gets Name
fruit2 = input("Give me a second thing: ")

x = 1
while x == 1:
	if fruit == "" :
		fruit = input("Give me a thing: ")
	else: 
		x = 0
y = 1
while y == 1:
	if fruit2 ==  "" :
		fruit2 = input("Give me a second thing: ")
	else: 
		y = 0
w = 1
while w == 1:
	if fruit[0] == " ":
		fruit = input("Give me a thing without a space in the front: ")
	else:
		w = 0
h = 1
while h == 1:
	if fruit2[0] == " ":
		fruit2 = input("Give me a second thing without a space in the front: ")
	else:
		h = 0
letter = len(fruit) #Gets Length of Name
letter2 = len(fruit2)

rand1 = randint(1,letter) #Gets A Certain # of Letters in the the name
rand2 = randint(1,letter2)

print(fruit[0:rand1] + fruit2[0:rand2])


