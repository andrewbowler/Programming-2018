num = int(input('Enter the number: '))
result = num
index = 1
def sum_function(x):
        global index
        global result
        if index == num:
                return 1
        else:
                result += index
                index += 1
                return sum_function(result)

sum_function(num)
print ('The number is ' + str(result))
