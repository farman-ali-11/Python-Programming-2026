
n = int(input("Enter value here: "))

for i in range(1, 15):
    print((n*2)*7)
    n += 3

if (n >= 15):
    print(f"The entered value is correct: {n}")

else:
    print("Value is not found")