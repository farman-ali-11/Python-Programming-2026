# Find greatest of three numbers

def greatest(a, b, c):
    
    if(a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    
    elif(c>a and c>b):
        return c
    
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

print(f"The greatest number is: {greatest(a, b, c)}")