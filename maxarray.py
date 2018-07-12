arr = [5,7,4,3]
def maxArray(x):
        if len(x) == 1:         # base case: array is only 1 long
                return x[0]     # RETURN IT!!
        else:
                return max(x[0], maxArray(x[1:]))       # return the max whether it's the very first value or a value after 

print (str(maxArray(arr)))

# I'm pretty sure this is cheating (max()) still so I'm gonna keep working on it if so
# I think I have a better understanding of recursion tho, just gotta turn the
# comand into derivative code if that makes sense
