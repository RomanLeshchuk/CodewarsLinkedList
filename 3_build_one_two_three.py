class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    if head is None:
        return Node(data)

    inserted = Node(data)
    inserted.next = head

    return inserted

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)
