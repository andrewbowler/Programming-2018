def isEven(n):
	if n == 1:
		return 'odd'
	elif n == 0:
		return 'even'
	else:
		return isEven(n - 2)
num = int(input('Input number: '))
print(isEven(num))