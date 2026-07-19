# Temperature Conversion

def tempt(n):
    return (n * 1.8) + 32


n = int(input("Enter the temperature in Celsius: "))
c = round(tempt(n), 2)
print(f"The temperature in Farenheit is: {c}°F")
