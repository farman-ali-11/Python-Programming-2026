
# sum(n-1) + n

def sum(n):
    if (n==0):
        return

    return sum(n-1)+n

n = int(input("Enter the value: "))