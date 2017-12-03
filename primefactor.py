#checks if the num is prime
def isPrimeNumber(primeNum):
	if primeNum > 1:
		for i in range(2,primeNum):
			if primeNum % i == 0:
				#the number is not prime
				return False
	return True #the number is prime 
myNum = input()
prime = isPrimeNumber(myNum) 
print(prime)

#function that works but not for big numbers
def prime_factors(n):
	factor = []
	for i in range(2, n):
		if n % i == 0: 
			if isPrimeNumber(i):
				factor.append(i)
	return factor
#array = prime_factors(600851475143)
#print(array)

#real function that works
def prime_factors2(primeNum):
	factor = [] #to hold all the factors of the num
	num = 2 #num which we divide the primeNum by
	#keep dividing by num and incrementing num until primeNum will no onlong be divisible by num
	while num * num < primeNum:
		#divide by num if it is divisible by num
		while primeNum % num == 0:
			#divide primeNum by num
			primeNum //= num
			#append num to the factor array
			factor.append(num)
			print(primeNum)
		#increment num when primeNum is no longer divisble by it
		num += 1
	#when we find that primeNum is equal to num; that num multiplied by num is greater than primeNum; when num divided by primeNum, after manipulation, is 1 we know it is the greatest prime factor 
	factor.append(primeNum)
	#return the factor
	return factor
theNum = prime_factors2(600851475143)
print(theNum)