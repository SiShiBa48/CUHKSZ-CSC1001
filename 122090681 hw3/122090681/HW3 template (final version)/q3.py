#### Please do not use input() function!!!
class ecosystem(object):

    def __init__(self, river_len, num_fish, num_bear, steps):
        #######initialization#######
        self.river_len = river_len
        self.num_fish = num_fish
        self.num_bear = num_bear
        self.steps = steps

    def simulation(self):
        import random
        ec = list()
        ec = ["N"] * self.river_len
        #print(ec)
        # You should follow the example format. Use print() tp display the result as given in AS3 read me.pdf. Do not use input()
        for i in range(self.num_fish):
            tt = True
            while tt:
                j = random.randint(0,self.river_len-1)
                if ec[j]=="N":
                    ec[j]="F"
                    tt = False
        for i in range(self.num_bear):
            tt = True
            while tt:
                j = random.randint(0,self.river_len-1)
                if ec[j]=="N":
                    ec[j]="B"
                    tt = False
        for i in range(self.steps):
            a = str(i+1)
            s = "The ecosystem at the beginning of the step "+a+":"
            print(s)
            print(ec)
            for i in range(self.river_len):
                if (ec[i]=="F")or(ec[i]=="B"):
                    a = ec[i]
                    k = random.randint(0,2)
                    if (k==0)and(i==0):
                        k=1
                    if (k==2)and(i==self.river_len-1):
                        k=1
                    if k==0:
                        if (ec[i]=="B"):
                            if ec[i-1]=="B":
                                if "N" in ec:
                                    tt = True
                                    while tt:
                                        j = random.randint(0,self.river_len-1)
                                        if ec[j]=="N":
                                            ec[j]="B"
                                            tt = False
                            if ec[i-1]=="F":
                                ec[i-1]="B"
                                ec[i]="N"
                            if ec[i-1]=="N":
                                ec[i-1]="B"
                                ec[i]="N"
                        if (ec[i]=="F"):
                            if ec[i-1]=="F":
                                if "N" in ec:
                                    tt = True
                                    while tt:
                                        j = random.randint(0,self.river_len-1)
                                        if ec[j]=="N":
                                            ec[j]="F"
                                            tt = False
                            if ec[i-1]=="B":
                                ec[i-1]="B"
                                ec[i]="N"
                            if ec[i-1]=="N":
                                ec[i-1]="F"
                                ec[i]="N"
                    if k==2:
                        if (ec[i]=="B"):
                            if ec[i+1]=="B":
                                if "N" in ec:
                                    tt = True
                                    while tt:
                                        j = random.randint(0,self.river_len-1)
                                        if ec[j]=="N":
                                            ec[j]="B"
                                            tt = False
                            if ec[i+1]=="F":
                                ec[i+1]="B"
                                ec[i]="N"
                            if ec[i+1]=="N":
                                ec[i+1]="B"
                                ec[i]="N"
                        if (ec[i]=="F"):
                            if ec[i+1]=="F":
                                if "N" in ec:
                                    tt = True
                                    while tt:
                                        j = random.randint(0,self.river_len-1)
                                        if ec[j]=="N":
                                            ec[j]="F"
                                            tt = False
                            if ec[i+1]=="B":
                                ec[i+1]="B"
                                ec[i]="N"
                            if ec[i+1]=="N":
                                ec[i+1]="F"
                                ec[i]="N"
                    print("Animal:",a,", Action:",k-1)
                    print("The current ecosystem after the action:")
                    print(ec)
                   
#eco = ecosystem(5,2,3,3)
#result = eco.simulation()

