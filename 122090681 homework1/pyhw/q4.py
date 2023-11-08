n = input()
try:
    n = int(n)
    print("m        m+1      m**(m+1)")
    for i in range(n):
        j = i+1
        k = i+2
        l = j**(j+1)
        j = str(j)
        k = str(k)
        l = str(l)
        print("%-8s" % j,"%-8s" % k,"%-8s" % l)
except:
    print("A correct number please")
