"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""


class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # Start writing your code.
        if self.size == 0:
            self.head = Node(data,self.tail)
            self.size = 1
        else:
            cur = self.head
            while cur.pointer != None:
                cur =  cur.pointer
            cur.pointer = Node(data,self.tail)   
            self.size = self.size + 1
        # End writing your code.


def count_node(node):
    # start writing your code.
    add = 0
    cur = node.pointer
    while cur != None:
        cur = cur.pointer
        add = add + 1
    return add
    # end writing your code.


# We will utilize the code similar to the following to check your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,-1]  # An example.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    print('The number of nodes in test_list is:')
    print(count_node(first_node))

