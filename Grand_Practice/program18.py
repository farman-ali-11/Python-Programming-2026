# Function with arguments

def fr(name, greeting="Best of luck.."):
    print(f"Hello, {name}")
    print(greeting)

fr("Farman Rajper", "You are the best..")
fr("Ahmed Khan")


def rf():
    print("Good Day")

rf()

def fun():
    print("Good Evening")
    print(f"Hey.. {rf()}")

fun()
fun()