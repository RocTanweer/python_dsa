# Making class for the node of linked list
class Node:

    # Each node have a value and a reference(default to None) to the next node in the list
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# d = Node('d')  # Pointing to None (meaning last node of the list(tail node))
c = Node('c')  # Having value of 'C' and pointing to next node d
b = Node('b', c)
a = Node('a', b)


D = Node('D')  # Pointing to None (meaning last node of the list(tail node))
C = Node('C', D)  # Having value of 'C' and pointing to next node d
B = Node('B', C)
A = Node('A', B)


def zipper_loop(head1, head2):
    '''Time: O(min(m, n)) | Space: O(1)'''
    current1 = head1
    current2 = head2

    while current1 != None and current2 != None:
        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        current2.next = next1
        current1 = next1
        current2 = next2

    current1 = head1

    while current1 != None:
        print(current1.val)
        current1 = current1.next


zipper_loop(A, a)
