class Node:
    '''class representing node of the linked list'''

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


d = Node('D')  # Pointing to None (meaning last node of the list(tail node))
c = Node('C', d)  # Having value of 'C' and pointing to next node d
b = Node('B', c)
a = Node('A', b)


def linked_find_loop(head, target):
    '''Time: O(n) | Space: O(1)'''
    current = head

    while current != None:
        if (current.val == target):
            return True
        current = current.next

    return False


result = linked_find_loop(a, 'G')
print(result)


def linked_find_recursion(head, target):
    '''Time: O(n) | Space: O(n)'''
    if (head.val == target):
        return True
    if (head == None):
        return False

    return linked_find_recursion(head.next, target)


result = linked_find_recursion(a, 'C')
print(result)
