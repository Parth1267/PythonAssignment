
p = int(input("enter p :"))
t = float(input("enter t :"))
r = int(input("enter r :"))


def compund_interest(p, r, t):
    a = p * (pow((1+r/100), t))
    ci = a - p
    print("compund interest is", ci)


print(compund_interest(p, r, t))
