def triangle(n, x):
	y = -1 * n + x
	if n == 0:
		return 1
	else:
		print(' ' * n + '* ' * y)
		return triangle(n - 1, x)
num = int(input())
triangle(num, num + 1)
