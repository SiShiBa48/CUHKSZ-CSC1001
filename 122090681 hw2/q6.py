def priqueen(ans):   #for output the answer and 
    global sum
    global allsol
    sum = sum + 1
   # print(sum)
   # print(ans)
    if sum == 48:
        allsol = ans

def pretty():
    for i in range(8):
        for j in range(8):
            if allsol[i]==j:
                print("|Q",end="")
            else:
                print("| ",end="")
        print("|")

def canq(n,ca,m):
    for i in range(n+1):
        if ca[i]==m: 
            return False
        if abs(i-(n+1))==abs(ca[i]-m): return False
    return True

def queen(n,que):
   # print(que)
    if n == 7:
        priqueen(que)
        return
    for i in range(8):
        if canq(n,que,i):
            s = que + [i]
            queen(n+1,s)

sol = [0]
sum = 0
allsol = []
#print(sol)
import random
for i in range(8):
    sol[0] = i
    queen(0,sol)
#print(allsol)
pretty()