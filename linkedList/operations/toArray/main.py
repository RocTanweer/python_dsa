# Making class for the node of linked list
class Node:

    # Each node have a value and a reference(default to None) to the next node in the list
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


d = Node('D')  # Pointing to None (meaning last node of the list(tail node))
c = Node('C', d)  # Having value of 'C' and pointing to next node d
b = Node('B', c)
a = Node('A', b)


def linked_list_to_array_loop(head):
    current = head
    array = []

    while (current != None):
        array.append(current.val)
        current = current.next
    return array


arr = linked_list_to_array_loop(a)
print(arr)


def find_values(head, array):
    if (head == None):
        return

    array.append(head.val)
    find_values(head.next, array)


def linked_list_to_array_recursion(head):
    array = []
    find_values(head, array)
    return array


arr2 = linked_list_to_array_recursion(a)
print(arr2)
