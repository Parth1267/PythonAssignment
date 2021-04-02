num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))


def maxnum(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


print(maxnum(num1, num2))
