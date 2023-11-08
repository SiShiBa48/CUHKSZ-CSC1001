def primenum(num):
    # a function to judge whether num is a prime number or not
    if num==1:
        return False
    for q in range(2,num-1):
        if num % q == 0:
            return False
    return True

def emirps_100():
    i = 1
    k = 13
    sum = 0
    while i<=100:
        l = k
        j = 0
        while l>0:
            q = l % 10
            j = j*10 + q
            l = l // 10
    # if j==k: continue 
        if (primenum(j)and primenum(k))and(j!=k):
            if sum==9: 
                i = i + 1
                print("%5d" %k)
                sum = 0
            else:
                sum = sum + 1
                i = i + 1
                print("%5d" %k,end="")
        k = k + 1
emirps_100()

