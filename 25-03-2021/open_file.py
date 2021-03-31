def main():
    f = open('hello.txt')
    for line in f:
        print(line.rstrip())


if __name__ == '__main__':
    main()
