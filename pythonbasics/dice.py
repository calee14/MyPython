from random import randint
print(randint(1, 6))
rollagain = "yes"
while rollagain == "yes":
	print("want to roll again?")
	i = input()
	if i == rollagain:
		print(randint(1,6))
	else:
		rollagain = "no"
