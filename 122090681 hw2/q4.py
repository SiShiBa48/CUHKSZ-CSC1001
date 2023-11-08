def isAnagram(s1,s2):
    dic1 = dict()
    dic2 = dict()
   # print(s1,s2)
    for i in range(len(s1)):
        if s1[i] in dic1:
            dic1[s1[i]] = dic1[s1[i]] + 1
         #   print("aa")
        else:
            dic1[s1[i]] = 1
            #print("bb")
    for i in range(len(s2)):
        if s2[i] in dic2:
            dic2[s2[i]] = dic2[s2[i]] + 1
        else:
            dic2[s2[i]] = 1
  #  print(dic1,dic2)
    a = list(dic1.items())
    b = list(dic2.items())
    a.sort()
    b.sort()
   # print(a,b)
    if len(a)!=len(b): return False
    for i in range(len(a)):
        if a[i]!=b[i]: return False
    return True
    
s1 = input()
s2 = input()
if isAnagram(s1,s2):
    print("is an anagram")
else:
    print("is not an anagram")