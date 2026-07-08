# Convert inches to cms

def inch_to_cms(n):
    return (n*2.54)

n = int(input("Enter value in Inches: "))
c = inch_to_cms(n)
print(f"The corresponding value in cms is: {c} Cm")
