fav = input("Enter the final account value:")
air = input("Enter the final interest rate:")
noy = input("Enter the number of years:")
fav = float(fav)
air = float(air)
noy = float(noy)
i = 1+air*0.01
#print(i)
j = i**noy
#print(j)
ida = fav/j
print("The initial value is: ",ida)
