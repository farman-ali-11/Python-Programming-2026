'''
Sum of n natural number
      sum(n-1) + n

'''

def sum(n):
    if (n==1):
        return 1

    return sum(n-1) + n

n = int(input("Enter the value: "))
b = sum(n)
print(f"The sum of {n} natural number is: {b}")