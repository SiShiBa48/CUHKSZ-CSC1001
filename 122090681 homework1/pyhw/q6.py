f = input("Please print a function ")
if f=="sin":
    try:
        from math import sin
        a,b = input("Please print the range ").split()
        n = input("Please print the number of sub-intervals ")
        a = int(a)
        b = int(b)
        n = int(n)
        k = 0
        for i in range(a,b):
            k = k + (b-a)/n*sin(a+(b-a)/n*(i-0.5))
        print(k)
    except:
        print("A correct range please ")
elif f=="cos":
    try:
        from math import cos 
        a,b = input("Please print the range ").split()
        n = input("Please print the number of sub-intervals ")
        a = int(a)
        b = int(b)
        n = int(n)
        k = 0
        for i in range(a,b):
            k = k + (b-a)/n*cos(a+(b-a)/n*(i-0.5))
        print(k)
    except:
        print("A correct range please ")
elif f=="tan":
    try:
        from math import tan
        a,b = input("Please print the range ").split()
        n = input("Please print the number of sub-intervals ")
        a = int(a)
        b = int(b)
        n = int(n)
        k = 0
        for i in range(a,b):
            k = k + (b-a)/n*tan(a+(b-a)/n*(i-0.5))
        print(k)
    except:
        print("A correct range please ")
else:
    print("The function is wrong ")