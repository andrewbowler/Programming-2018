num = int(input('Enter the number: '))

def sum_function(x):
        if x == 1:
                return 1
        else:
                return x + sum_function(x - 1)

print ('The number is ' + str(sum_function(num)))
