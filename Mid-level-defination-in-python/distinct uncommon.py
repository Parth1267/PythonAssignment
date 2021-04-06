def disticntUncommonDigits(a,b):

    a = str(a)
    b=str(b)

    a =list(map(int,a))
    b =list(map(int,b))

    a =set(a)
    b = set(b)

    lis = a.symmetric_difference(b)

    lis = list(lis)
    lis.sort(reverse=True)


    for i in lis:
        print(i)


a=154   
b=2345

disticntUncommonDigits(a,b)