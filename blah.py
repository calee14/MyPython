print("Hello World!")
print("What is your name") #ask for name
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is:") 
print(str(len(myName)) + " characters")
print("What is your age?")
myAge = float(input())
comAge = 1
diff = myAge - comAge
if diff > 1 :
	g = " years younger than me"
else:
	g = " years older than me"
print("You are " + str(diff) + g)
