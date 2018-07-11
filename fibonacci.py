num = int(input('Enter #: '))
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci (n - 2)
print(str(fibonacci(num)))
#a(n) = a(n-1) + a(n-2)
""" I followed the recursion formula
I learned in discrete--did NOT expect
it to work, thought it would be MUCH harder
but I guess it works for a reason :^) """
