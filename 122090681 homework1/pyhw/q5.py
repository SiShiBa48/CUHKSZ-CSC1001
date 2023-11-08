def primenum(num):
    # a function to judge whether num is a prime number or not
    if num==1:
        return False
    for q in range(2,num-1):
        if num % q == 0:
            return False
    return True

try:
    n = input()
    n = int(n)
    print("The prime number smaller than ",n," include:")
    k = 0
    #k for output 8 number
    for i in range(n-1):
        j = i+1
        if primenum(j):
            if k==7:
                print(j)
                k = 0
            else:
                print(j,end=" ")
                k = k+1

except:
    print("A correct number please")
