def gcd(x, y):
	r = x % y		# r is equal to the remainder;
	if r == 0:		# if there is none, y is the gcd per Euclidean algorithm
		return y
	else:					# otherwise, try again with the dividend and remainder
		return gcd(x, r)
	
a = int(input('Input #1: '))
b = int(input('Input #2: '))
print('GCD is ' + str(gcd(a, b)))