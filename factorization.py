import math										# For sqrt()

def factorization(x, y = 2):					# Takes a number and a prime (starts with 2)
	if isPrime(y) == False:						# If y (divisor) is not a prime number, increment until it is (default: 2)
		y += 1
		return factorization(x, y)
	elif isPrime(x) == True:					# If x (dividend) is a prime number, it's the final factor
		return int(x)
	elif isPrime(x) == False:
		if x % y == 0:							# If y divides x, print y and repeat with x = x / y
			print(int(y))
			return factorization(x / y, y)
		elif x % y != 0:						# If not, bump y up 1 which will trigger the first IF statement to increment y
			y += 1
			return factorization(x, y)

def isPrime(n, m = 2):							# Takes a number to test and a potential factor (default: 2)
	if m > math.sqrt(n):						# If m increments above sqrt(n) then it's a prime
		return True
	elif n % m == 0:							# If the numbers divide evenly before m > sqrt(n) it's composite
		return False
	else:										# If both conditions fail, increment m
		return isPrime(n, m + 1)

num = int(input('Input a number: '))
print(factorization(num))