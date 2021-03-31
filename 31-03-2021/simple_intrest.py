# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
p = int(input("enter p :"))
t = int(input("enter t :"))
r = int(input("enter r :"))


def simple_interest(p, t, r):

    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si


# Driver code
print(simple_interest(p, t, r))
