# dmeostrate the use of keyword-only argumtnets

# use keyword-only arguments to help ensure code clarity

def myFunc(args1, args2, *, supperExcep=False):
    print(args1, args2, supperExcep)


def main():
    # try to call function without the kwyword
    # myFunc(10,20,true)
    myFunc(10, 20, supperExcep=True)


if __name__ == "__main__":
    main()
