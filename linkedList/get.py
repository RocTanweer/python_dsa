class Node:
    '''class representing node of the linked list'''

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


d = Node('D')  # Pointing to None (meaning last node of the list(tail node))
c = Node('C', d)  # Having value of 'C' and pointing to next node d
b = Node('B', c)
a = Node('A', b)


def get_node_value_loop(head, index):
    '''Time: O(n) | Space: O(1)'''
    counter = 0
    current = head

    while current != None:
        if (counter == index):
            return current.val
        counter += 1
        current = current.next

    return None


result = get_node_value_loop(a, 2)
print(result)


def get_node_value_recursion(head, index, counter=0):
    '''Time: O(n) | Space: O(n)'''
    if (head == None):
        return None

    if counter == index:
        return head.val
    else:
        counter += 1

    return get_node_value_recursion(head.next, index, counter)


result = get_node_value_recursion(a, 3)
print(result)
