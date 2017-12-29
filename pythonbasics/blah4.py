friendNames = []
while True:
    print("Enter the name of friend " + str(len(friendNames) + 1) +
      " (Or enter nothing to stop.):")
    name = input()
    if name == '':
        break
    friendNames = friendNames + [name] # list concatenation
print("Your friend's names are:")
for name in friendNames:
    print('  ' + name)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print("Enter a friend's name")
nameInput = input() # input for name that is going to check in the loop
if nameInput not in friendNames:
	print("Sry " + nameInput + " is not my friend Yay!")
else: 
	print("You made a excellent choice choosing " + nameInput)