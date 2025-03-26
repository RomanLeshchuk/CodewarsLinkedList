class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    if head is None:
        return Node(data)

    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = Node(data)

    return head

def build_one_two_three():
    return push(push(push(None, 1), 2), 3)
