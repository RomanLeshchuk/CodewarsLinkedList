class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    new_head = head.next
    head.next = new_head.next
    new_head.next = head

    head.next = swap_pairs(head.next)

    return new_head
