class User:
	def __init__(self, user, money):
		self.user = user
		self.money = money

	def makeDeposit(self,amountGoingIn):
		self.money = str(int(self.money) + int(amountGoingIn))

	def makeWithdraw(self,amountGoingOut):
		if int(self.money) < int(amountGoingOut):
			raise ValueError
		else:
			self.money = str(int(self.money) - int(amountGoingOut))

class textChecker:
	def troll(self, inputTroll):
		if inputTroll == "":
			raise ValueError

	def troll2(self, inputTroll2):
		for char in inputTroll2:
			if char.isalpha():
				raise ValueError

def main():
	checker = textChecker()
	userName = input("Type your name: ")
	checker.troll(userName) #Check

	accountAmount = input("How much is in ur bank account: ")
	checker.troll2(accountAmount) #Check

	bankAccount = User(userName, accountAmount)
	
	x = 1
	while x == 1:
		correctUser = input("Which bankAccount would you like to use: ")
		while correctUser == "":
			correctUser = input("Which bankAccount would you like to use: ")	
		if correctUser == bankAccount.user:
			drawOrDeposit = input("Would you like to withdraw or deposit: ")
			checker.troll(drawOrDeposit) #Check
			if drawOrDeposit == "withdraw":
				moneyTakingOut = input("How much: ")
				checker.troll(moneyTakingOut) #Check
				bankAccount.makeWithdraw(moneyTakingOut)
			if drawOrDeposit == "deposit":
				moneyPuttingIn = input("How much are you puttin in: ")
				checker.troll(moneyPuttingIn) #Check
				bankAccount.makeDeposit(moneyPuttingIn)
			if drawOrDeposit == "exit":
				raise ValueError
	print("$" + bankAccount.money)
	print(bankAccount.user) 		

if __name__ == '__main__':
	main()
		

