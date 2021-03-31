# demonstrate the use of variable argument lists

# define a function that takes variable argument

def addition(base, *args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # pass different argument
    print(addition(20, 50, 5, 15))
    print(addition(1, 2, 3))

    # pass an existing list
    myNum = [1, 50, 20]
    print(addition(*myNum))


if __name__ == "__main__":
    main()
