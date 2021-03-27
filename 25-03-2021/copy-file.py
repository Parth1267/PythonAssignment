def main():
    f = open('hello.txt', 'rt')
    c = open('hello-copy.txt', 'wt')
    for line in f:
        print(line.rstrip(), file=c)
        print('.', end='', flush=True)
    c.close()
    print('\ndone.')

    if __name__ == '__main__': main()
