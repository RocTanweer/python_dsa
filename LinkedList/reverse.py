class Node:
    '''class representing node of the linked list'''

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


d = Node('D')  # Pointing to None (meaning last node of the list(tail node))
c = Node('C', d)  # Having value of 'C' and pointing to next node d
b = Node('B', c)
a = Node('A', b)


def reverse_loop(head):
    '''Time: O(n) | Space: O(1)'''
    current = head
    prev = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev.val


# result = reverse_loop(a)
# print(result)


def reverse_recursion(head, prev=None):
    '''Time: O(n) | Space: O(n)'''
    if head == None:
        return prev.val

    next = head.next

    return reverse_recursion(next, head)


result = reverse_recursion(a)
print(result)
