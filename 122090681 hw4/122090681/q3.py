"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""


def HanoiTower(n, from_rod ='A',aux_rod ='B',to_rod ='C'):
    global result_list
    result_list = []
    # Start writing your code.
    hano(n,"A","B","C")
    # End writing your code.
    return result_list

def hano(n, from_rod ='A',aux_rod ='B',to_rod ='C'):
    if n == 1:
        st = from_rod + " --> " + to_rod
        result_list.append(st)
    else:
        hano(n-1,from_rod,to_rod,aux_rod)
        hano(1,from_rod,aux_rod,to_rod)
        hano(n-1,aux_rod,from_rod,to_rod)
"""
You should store each line your output in result_list defined above.
For example, if the outputs of print() are: 
                A --> C
                A --> B
then please store them in result_list:

strs = "A --> C"
result_list.append(strs)
strs = "A --> B"
result_list.append(strs)

Thus, once you want to print something, please store them in result_list immediately, 
rather than utilizing print() to print it. 
Don't miss the space! For example, don't output:
                A-->C
                A-->B

We will utilize the code similar to the following to check your answer.
"""

if __name__ == '__main__':
    n = 3
    result_list = HanoiTower(n)
    for item in result_list:
        print(item)
