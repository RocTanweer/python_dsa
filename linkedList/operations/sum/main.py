# Making class for the node of linked list
class Node:

    # Each node have a value and a reference(default to None) to the next node in the list
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


d = Node(7)  # Pointing to None (meaning last node of the list(tail node))
c = Node(3, d)  # Having value of 'C' and pointing to next node d
b = Node(8, c)
a = Node(2, b)


def linked_list_sum_loop(head):
    current = head
    sum = 0

    while (current != None):
        sum += current.val
        current = current.next
    return sum


arr = linked_list_sum_loop(a)
print(arr)


def linked_list_sum_recursion(head):
    if head == None:
        return 0
    return head.val + linked_list_sum_recursion(head.next)


arr2 = linked_list_sum_recursion(a)
print(arr2)
