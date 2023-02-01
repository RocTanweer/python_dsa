class Node:
    '''Class for node of the Linked list'''

    def __init__(self, val):
        '''Each node having a value(val) and address of the next node(default to None)'''
        self.val = val
        self.next = None


# Creating nodes of linked list
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

# a node pointing to b node
a.next = b
# b node pointing to c node
b.next = c
# c node pointing to d node
c.next = d

# d node pointing to 'None' default value


def insert__loop(head, node, pos):
    current = head
    prev = None
    counter = 0

    while current != None:

        if pos == counter and prev == None:
            node.next = head
            return node

        if pos == counter and prev != None:
            nextOfPrev = prev.next
            prev.next = node
            node.next = nextOfPrev
            return head

        if pos == counter + 1 and current.next == None:
            current.next = node
            return head

        prev = current
        current = current.next
        counter += 1


q = Node('q')

newHead = insert__loop(a, q, 4)

cu = newHead
while cu != None:
    print(cu.val)
    cu = cu.next
