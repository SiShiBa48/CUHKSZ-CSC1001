def getdigit(number):
    i = int(number)
    l = [2,4,6,8,1,3,5,7,9,0]
    return l[i-1]

def sumofoddplace(number):
    sum = 0
    for i in range(len(number)):
        if i % 2 == 0:
            sum = sum + int(getdigit(number[i]))
    return sum

def sumofdoubleplace(number):
    sum = 0
    for i in range(len(number)):
        if i % 2 == 1:
            sum = sum + int(number[i])
    return sum

def isvalid(number):
    if number % 10 == 0:
        return True
    else:
        return False

dig = input("please input a card number ")
odd = sumofoddplace(dig)
dou = sumofdoubleplace(dig)
#print(odd,dou)
sum = odd + dou
if isvalid(sum): 
    print("The card is valid")
else:
    print("The card is invalid")
