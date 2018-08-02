# For sqrt()
import math

# Function to find prime factors
def factorization(primeArr, x, y = 2):
	if isPrime(y) == False:
		y += 1
		return factorization(primeArr, x, y)
	elif isPrime(x) == True:
		primeArr.extend([int(x)])
		return primeArr
	elif isPrime(x) == False:
		if x % y == 0:
			primeArr.extend([y])
			return factorization(primeArr, x / y, y)
		elif x % y != 0:
			y += 1
			return factorization(primeArr, x, y)

# Function to find if a number is prime
def isPrime(n, m = 2):
	if m > math.sqrt(n):
		return True
	elif n % m == 0:
		return False
	else:
		return isPrime(n, m + 1)

# User input
num = int(input('Input a number: '))
primeList = []
factorization(primeList, num)

# Example of array now contained in "primeList"
print('The prime factors are: ' + str(primeList))