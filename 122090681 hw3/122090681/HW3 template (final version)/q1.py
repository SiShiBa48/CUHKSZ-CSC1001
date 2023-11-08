#### Please do not use input() function!!!
class Flower(object):
    def __init__(self,name,petal,price):
        self.name = name
        self.petal = petal
        self.price = price
    def Information(self):
        if isinstance(self.name,int):
           s = "The input of the flower name is incorrect. A string is required."
           return s
        if isinstance(self.petal,str):
            s= "The input of the number of petals is incorrect. An integer is required."
            return s
        if isinstance(self.price,str):
            s= "The input of the number of petals is incorrect. An float is required."
            return s
        a = str(self.petal)
        b = str(self.price)
        s = "Here is the information of your flower. Name: " + self.name + ", Number of petals: " + a + ", price: " + b
        return s
#flower = Flower("juice","eee",7.82)
#result = flower.Information()
#print(result)