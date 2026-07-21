
n = int(input("Enter value here: "))

for i in range(1, 10):
    print((n*2)*3)
    n += 3

if (n >= 13):
    print(f"The entered value is correct: {n}")

else:
    print("Value is not found")