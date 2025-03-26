class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(data)

def build_one_two_three():
    head = Node(1)
    push(head, 2)
    push(head, 3)
    return head
