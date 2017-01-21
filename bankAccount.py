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
	def askForUser(self):
		isCorrectUser = input("Which bankAccount would you like to use: ")
		return isCorrectUser
class textChecker:
	def troll(inputTroll):
		while inputTroll == "":
			raise ValueError 
	def troll2(inputTroll2):
		 

def main():
	checker = textChecker()
	userName = input("Type your name: ")
	checker.troll(userName)
	accountAmount = input("How much is in ur bank account: ")
	checker.troll(accountAmount)
	bankAccount = User(userName, accountAmount)
	print(bankAccount.user)
	x = 1
	while x == 1:
		correctUser = bankAccount.askForUser()
		while correctUser == "":
			correctUser = bankAccount.askForUser()	
		if correctUser == bankAccount.user:
			drawOrDeposit = input("Would you like to withdraw or deposit: ")
			checker.troll(drawOrDeposit)
		if drawOrDeposit == "withdraw":
			moneyTakingOut = input("How much: ")
			checker.troll(moneyTakingOut)
			bankAccount.makeWithdraw(moneyTakingOut)
		if drawOrDeposit == "deposit":
			moneyPuttingIn = input("How much are you puttin in: ")
			checker.troll(moneyPuttingIn)
			bankAccount.makeDeposit(moneyPuttingIn)
		if drawOrDeposit == "":
			x = 0
	print("$" + bankAccount.money) 		

if __name__ == '__main__':
	main()
		

