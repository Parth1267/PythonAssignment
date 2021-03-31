num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

print("1. addition")
print("2. subtrtaction")
print("3. multiplication")
print("4. division")

cal = input("Enter which operator use :")


def add(num1, num2, cal):

    return num1 + num2


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


if cal == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif cal == '2':
    print(num1, "-", num2, "=", sub(num1, num2))
elif cal == '3':
    print(num1, "*", num2, "=", mul(num1, num2))
elif cal == '4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("invid out out")
