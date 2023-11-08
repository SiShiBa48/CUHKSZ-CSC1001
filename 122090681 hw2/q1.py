def sqrt(n):
    n = float(n)
    nextguess = 0.0
    lastguess = n
    while True:
        nextguess = (lastguess+(n/lastguess))/2
        if abs(nextguess-lastguess)<=0.0001: break
   # print(nextguess)
        lastguess = nextguess
    print(lastguess)
n = input()
sqrt(n)