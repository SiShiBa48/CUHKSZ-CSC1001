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


def quick_sort(node):
    # Start writing your code.
    less = SinglyLinkedList()
    equal = SinglyLinkedList()
    greater = SinglyLinkedList()
    if node.pointer == None:
        return node
    i = node.element
    cur = node
    while cur.pointer != None:
        if i > cur.element:
            less.insert(cur.element)
        if i == cur.element:
            equal.insert(cur.element)
        if i < cur.element:
            greater.insert(cur.element)  
        cur = cur.pointer
    if i > cur.element:
            less.insert(cur.element)
    if i == cur.element:
        equal.insert(cur.element)
    if i < cur.element:
        greater.insert(cur.element)  
    if less.head != None:
        e = quick_sort(less.head)
    if greater.head != None:
        q = quick_sort(greater.head)  
    ans = SinglyLinkedList()
    if less.head != None:
        while e.pointer != None:
            ans.insert(e.element)
            e = e.pointer
        ans.insert(e.element)
    if equal.head != None:
        c = equal.head
        while c.pointer != None:
            ans.insert(c.element)
            c = c.pointer
        ans.insert(c.element)
    if greater.head != None:
        while q.pointer != None:
            ans.insert(q.element)
            q = q.pointer
        ans.insert(q.element)
    return ans.head
    # End writing your code.


# We will utilize the code similar to the following to check your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,5]  # An example.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    print('The number of nodes in test_list is:')
    p = quick_sort(first_node)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)
    
