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


def print_linked_list_loop(head):
    current = head
    while current != None:
        print(current.val)
        current = current.next


print_linked_list_loop(a)


def print_linked_list_recursion(head):
    if head == None:
        return
    print(head.val)
    print_linked_list_recursion(head.next)


print('\n')

print_linked_list_recursion(a)
